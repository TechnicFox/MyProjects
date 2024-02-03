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
pygame.display.set_caption('Catch')

background = pygame.transform.scale(pygame.image.load('image/background.png'),resolution)
sprite1 = pygame.transform.scale(pygame.image.load('image/sprite1.png'),(100,100))
sprite2 = pygame.transform.scale(pygame.image.load('image/sprite2.png'),(100,100))

x1 = 250
y1 = 250
x2 = 250
y2 = 250
speed = 5


while True:

    for i in pygame.event.get():
        
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            start_draw = True
            start_pos = i.pos
        elif i.type == pygame.MOUSEMOTION and start_draw:
            end_pos = i.pos
            width = end_pos[0]-start_pos[0]
            height = end_pos[1]-start_pos[1]
            shape = pygame.draw.rect(window,red,(start_pos[0],start_pos[1],width,height))
        elif i.type == pygame.MOUSEBUTTONDOWN and i.button == 3:
            start_draw2 = True
            start_pos = i.pos    
        elif i.type == pygame.MOUSEMOTION and start_draw2:
            end_pos = i.pos
            width = end_pos[0]-start_pos[0]
            height = end_pos[1]-start_pos[1]
            shape = pygame.draw.rect(window,black,(start_pos[0],start_pos[1],-width,-height))

        if i.type == pygame.MOUSEBUTTONUP and i.button == 1:
            start_draw = False

    pygame.display.update()
    clock.tick(FPS)

            
            