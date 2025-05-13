import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
import yt_dlp
import os
import asyncio

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your music/video bot. Use /play [song name] to play a song or /video [video name] to get a video!')

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        if not context.args:
            await update.message.reply_text('Please provide a song name. Usage: /play [song name]')
            return

        song_name = ' '.join(context.args)
        await update.message.reply_text(f'Searching for "{song_name}"...')

        keyboard = [
            [InlineKeyboardButton("Recommended (256kbps)", callback_data='audio_256')],
            [InlineKeyboardButton("Low (64kbps)", callback_data='audio_64'),
             InlineKeyboardButton("Medium (128kbps)", callback_data='audio_128')],
            [InlineKeyboardButton("High (192kbps)", callback_data='audio_192'),
             InlineKeyboardButton("Very High (256kbps)", callback_data='audio_256')],
            [InlineKeyboardButton("Extreme (320kbps)", callback_data='audio_320')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('Please select the audio quality:', reply_markup=reply_markup)

        context.user_data['song_name'] = song_name
    except Exception as e:
        logger.error(f"Error in play command: {str(e)}")
        await update.message.reply_text("An error occurred. Please try again later.")

async def video(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        if not context.args:
            await update.message.reply_text('Please provide a video name. Usage: /video [video name]')
            return

        video_name = ' '.join(context.args)
        await update.message.reply_text(f'Searching for "{video_name}"...')

        keyboard = [
            [InlineKeyboardButton("360p", callback_data='video_360'),
             InlineKeyboardButton("480p", callback_data='video_480')],
            [InlineKeyboardButton("720p", callback_data='video_720')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('Please select the video quality:', reply_markup=reply_markup)

        context.user_data['video_name'] = video_name
    except Exception as e:
        logger.error(f"Error in video command: {str(e)}")
        await update.message.reply_text("An error occurred. Please try again later.")

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        query = update.callback_query
        await query.answer()

        if query.data.startswith('audio_'):
            quality = query.data.split('_')[1]
            await download_audio(update, context, quality)
        elif query.data.startswith('video_'):
            quality = query.data.split('_')[1]
            await download_video(update, context, quality)
    except Exception as e:
        logger.error(f"Error in button callback: {str(e)}")
        await update.callback_query.message.reply_text("An error occurred. Please try again later.")

async def download_audio(update: Update, context: ContextTypes.DEFAULT_TYPE, quality: str) -> None:
    try:
        song_name = context.user_data.get('song_name')
        if not song_name:
            await update.callback_query.message.reply_text("Please provide a song name first.")
            return

        status_message = await update.callback_query.message.reply_text(
            f'Downloading "{song_name}" with {quality}kbps quality...'
        )

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': quality,
            }],
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': True,
            'no_warnings': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{song_name}", download=True)
            filename = ydl.prepare_filename(info['entries'][0]).rsplit(".", 1)[0] + ".mp3"

        await status_message.edit_text("Upload starting...")
        
        with open(filename, 'rb') as audio_file:
            await update.callback_query.message.reply_audio(
                audio=audio_file,
                title=info['entries'][0]['title'],
                duration=info['entries'][0]['duration']
            )
        
        os.remove(filename)
        await status_message.delete()

    except Exception as e:
        logger.error(f"Error in audio download: {str(e)}")
        await update.callback_query.message.reply_text(
            "Sorry, there was an error downloading the audio. Please try again."
        )

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE, quality: str) -> None:
    try:
        video_name = context.user_data.get('video_name')
        if not video_name:
            await update.callback_query.message.reply_text("Please provide a video name first.")
            return

        status_message = await update.callback_query.message.reply_text(
            f'Downloading "{video_name}" in {quality}p...'
        )

        ydl_opts = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]',
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': True,
            'no_warnings': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{video_name}", download=True)
            filename = ydl.prepare_filename(info['entries'][0])

        await status_message.edit_text("Upload starting...")
        
        with open(filename, 'rb') as video_file:
            await update.callback_query.message.reply_video(
                video=video_file,
                caption=info['entries'][0]['title']
            )
        
        os.remove(filename)
        await status_message.delete()

    except Exception as e:
        logger.error(f"Error in video download: {str(e)}")
        await update.callback_query.message.reply_text(
            "Sorry, there was an error downloading the video. Please try again."
        )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        await update.message.reply_text(update.message.text)
    except Exception as e:
        logger.error(f"Error in echo: {str(e)}")


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Stoping the Bot....')

def main() -> None:
    try:
        # Replace with your bot token
        application = ApplicationBuilder().token("7484052645:AAHKSDPrzTR8ULPcrPtPEy_bUn5ty1zztXw").build()
        
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("play", play))
        application.add_handler(CommandHandler("video", video))
        application.add_handler(CommandHandler("stop", stop))
        application.add_handler(CallbackQueryHandler(button_callback))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
        
        application.run_polling()
    except Exception as e:
        logger.error(f"Error in main: {str(e)}")

if __name__ == '__main__':
    main()

"""
@kavya_musicBot is the most advanced music+video streaming Bot
*youtube music+video downloader.
* written from scratch, making it stable and less  crashes with attractive thumbnils.
*start, play, video, stop support.
*English support.
developed by:- @epsiloncreations
"""
