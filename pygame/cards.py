import pygame 
import sys
import random


pygame.init()

width,height = 700,350
FPS = 60
clock = pygame.time.Clock()
score = 0

white = (255,255,0)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (128,0,128)


window = pygame.display.set_mode((width,height))
window.fill('white')
pygame.display.set_caption('Remember cards')

orginal_colors = [white,black,red,blue,green,purple]
circle_radius = 50
circle_pairs = orginal_colors*2
random.shuffle(circle_pairs)
original_circles_pos = []
for i in range(6):
    for j in range(2):
        center_x = ((width / 6) * (i + 1)) - (width / 12)
        center_y = ((400 / 3) * (j + 1)) - (height / 6) + 50
        original_circles_pos.append((center_x,center_y))

colors = orginal_colors.copy()
circles_pos = original_circles_pos.copy()

font = pygame.font.SysFont('Arial',50)

for i in range(len(circle_pairs)):
    pos = original_circles_pos[i]
    col = circle_pairs[i]
    pygame.draw.circle(window,col,pos,circle_radius)
pygame.display.update()
pygame.time.wait(5000)

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(FPS)
    pygame.display.update()