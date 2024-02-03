import pygame
import sys

resolution = (500,500)
FPS = 60
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

pygame.init()

window = pygame.display.set_mode(resolution)
pygame.display.set_caption('Rectangle')

x = resolution[0] // 2
y = resolution[1] // 2
speed = 10

w=a=s=d=False

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                w=True
            if i.key == pygame.K_DOWN:
                s=True
            if i.key == pygame.K_LEFT:
                a=True
            if i.key == pygame.K_RIGHT:
                d=True
        elif i.type == pygame.KEYUP:
            w=a=s=d=False
    if w:
        y-=speed
    if s:
        y+=speed
    if d:
        x+=speed
    if a:
        x-=speed
    window.fill(white)
    pygame.draw.rect(window,red,(x,y,resolution[0] // 5,resolution[1] // 5))
    pygame.display.update()
    clock.tick(FPS)
