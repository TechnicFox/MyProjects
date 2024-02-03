import pygame
import sys

resolution = (500,500)
FPS = 120
clock = pygame.time.Clock()
size_x = 50
size_y = 50

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
speed = 1

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0:
        x-=speed
    if keys[pygame.K_RIGHT] and x<resolution[0]-size_x:
        x+=speed
    if keys[pygame.K_UP] and y>0:
        y-=speed
    if keys[pygame.K_DOWN] and y<resolution[1]-size_y:
        y+=speed
    window.fill(white)
    pygame.draw.rect(window,red,(x,y,size_x,size_y))
    pygame.display.update()
    clock.tick(FPS)
