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

background = pygame.transform.scale(pygame.image.load('pygame/images/background.png'),resolution)
sprite1 = pygame.transform.scale(pygame.image.load('pygame/images/sprite1.png'),(100,100))
sprite2 = pygame.transform.scale(pygame.image.load('pygame/images/sprite2.png'),(100,100))
x1 = 250
y1 = 250
x2 = 250
y2 = 250
speed = 5



while True:
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))
    for i in pygame.event.get():  
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keyboard = pygame.key.get_pressed()
    if keyboard[pygame.K_LEFT] and x1>0:
        x1-=speed
    if keyboard[pygame.K_RIGHT] and x1<400:
        x1+=speed
    if keyboard[pygame.K_DOWN] and y1<400:
        y1+=speed
    if keyboard[pygame.K_UP] and y1>0:
        y1-=speed
    if keyboard[pygame.K_a] and x2>0:
        x2-=speed
    if keyboard[pygame.K_d] and x2<400:
        x2+=speed
    if keyboard[pygame.K_s] and y2<400:
        y2+=speed
    if keyboard[pygame.K_w] and y2>0:
        y2-=speed
    if (x1<x2+50 and x1>x2-50) and (y1<y2+50 and y1>y2-50):
        window.blit(pygame.transform.scale(pygame.image.load('pygame/images/pngwing.png'),(300,300)),(x1-150,y1-150))
    
    pygame.display.update()
    clock.tick(FPS)        