import asyncio

async def say_hello():
    print("Hello waiting for 5 sec")
    await asyncio.sleep(5)
    print("World!")


async def main():
    await say_hello()
asyncio.run(main())
