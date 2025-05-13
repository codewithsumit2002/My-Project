import pygame
import sys
import random

pygame.init()
FPS = 15
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0) 
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
VELOCITY = 10
SNAKE_WIDTH = 15
APPLE+SIZE = 20
TOP_WIDTH 40
small_font = pygame.font.SysFont('Courier New', 25)
medium_font = pygame.font.SysFont('Courier New', 20, True)
large_font = pygame.font.SysFont('Courier New', 40, True, True)
clock = pygame.time.Clock()
canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')
snake_img = pygame.image.load('head.png')
apple_img = pygame.image.load('apple2.png')
tail_img = pygame.image.load('tail1.png')
apple_img_rect = apple_img.get_rect()

def start_game():
    canvas.fill(BLACK)
    start_font1 = large_font.render("Welcome to snake game", True, BLUE)
    start_font2 = medium_font.render("Play Game", True, BLACK, GREEN)
    start_font3 = medium_font.render("Instructions", True, BLACK, GREEN)
    start_font4 = medium_font.render("Quit", True, RED, GREEN)
    start_font1_rect = start_font1.get_rect()
    start_font2_rect = start_font2.get_rect()
    start_font3_rect = start_font3.get_rect()
    start_font4_rect = start_font4.get_rect()
    start_font1_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 100)
    start_font2_rect.center = (WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT/2 + 50)
    start_font3_rect.center = (WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT / 2 + 100)
    start_font4_rect.center = (WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT/2 + 150)
    canvas.blit(start_font1, start_font1_rect)
    canvas.blit(start_font2, start_font2_rect)
    canvas.blit(start_font3, start_font3_rect)
    canvas.blit(start_font4, start_font4_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameloop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_font3_rect.left and x < start_font3_rect.right:
                    if y > start_font3_rect.top and y < start_font3_rect.bottom:
                        start_inst(start_font1, start_font1_rect)
                if x > start_font2_rect.left and x < start_font2_rect.right:
                    if y > start_font2_rect.top and y < start_font2_rect.bottom:
                        gameloop()
                if x > start_font4_rect.left and x < start_font4_rect.right:
                    if y > start_font4_rect.top and y < start_font4_rect.bottom:
                        pygame.quit()
                        sys.exit()
        pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

 def start_inst(start_font1, start_font1_rect):
    canvas.fill(BLACK)
    canvas.blit(start_font1, start_font1_rect)
    start_inst1 = small_font.render("--> Do not cross the edges, else you will be dead", True, BLUE)
    start_inst2 = small_font.render("--> Keep eating the red apples", True, BLUE)
    start_inst3 = small_font.render("--> Do not cross over yourself", True, BLUE)
    start_inst4 = small_font.render("--> Keep playing......", True, BLUE)
    start_inst5 = medium_font.render("<<BACK", True, RED, YELLOW)
    start_inst5_rect = start_inst5.get_rect()
    start_inst5_rect.center = (WINDOW_WIDTH-100, WINDOW_HEIGHT - 100)
    canvas.blit(start_inst1, (WINDOW_WIDTH/8, WINDOW_HEIGHT/2))
    canvas.blit(start_inst2, (WINDOW_WIDTH/8, WINDOW_HEIGHT/2 + 30))
    canvas.blit(start_inst3, (WINDOW_WIDTH/8, WINDOW_HEIGHT/2 + 60))
    canvas.blit(start_inst4, (WINDOW_WIDTH/8, WINDOW_HEIGHT/2 + 90))
    canvas.blit(start_inst5, start_inst5_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_inst5_rect.left and x < start_inst5_rect.right:
                    if y > start_inst5_rect.top and y < start_inst5_rect.bottom:
                        start_game()
        pygame.display.update()
