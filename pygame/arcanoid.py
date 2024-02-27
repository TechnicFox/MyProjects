import pygame
import sys
import random

pygame.init()

resolution = (800,600)
FPS = 120
clock = pygame.time.Clock()
size_x = 50
size_y = 50
score = 0

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

block_width, block_height = 80,60
platform_width, platform_heigth = 150,20
platform_x, platform_y = resolution[0]/2,550

ball_radius = 10
ball_x, ball_y = platform_x,platform_y-50
speed_y = -2
speed_x = random.choice([-2,2])

blocks = []

for i in range(6):
    for j in range(9):
        block_x = j*(block_width+10)
        block_y = i*(block_height+10)
        blocks.append(pygame.Rect(block_x,block_y,block_width,block_height))


window = pygame.display.set_mode(resolution)
pygame.display.set_caption('Arcanoid.io')

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform_x > 0:
        platform_x -= 5
    if keys[pygame.K_RIGHT] and platform_x < resolution[0]-platform_width:
        platform_x += 5
    ball_x += speed_x
    ball_y += speed_y
    if ball_x <= 0 or ball_x >= resolution[0]-ball_radius:
        speed_x = -speed_x 
    if ball_y <= 0:
        speed_y = -speed_y

    if ball_y >= resolution[1]:
        print("YOU LOOSER!!!")
        pygame.quit()
        sys.exit()
    if platform_x <= ball_x <= platform_x+platform_width and platform_y <= ball_y <= platform_y + platform_heigth:
        speed_y = -speed_y
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x,ball_y,ball_radius,ball_radius)):
            speed_y = -speed_y
            blocks.remove(block)
    window.fill(white)
    
    pygame.draw.rect(window, red, (platform_x,platform_y,platform_width,platform_heigth))
    
    for i in blocks:
        pygame.draw.rect(window,green,i)
    pygame.draw.circle(window, blue, (ball_x,ball_y), ball_radius)
    print(len(blocks))
    if len(blocks) <= 0:
        print("YOU WIN!!!")
        pygame.quit()
        sys.exit()
    clock.tick(FPS)
    pygame.display.update()
