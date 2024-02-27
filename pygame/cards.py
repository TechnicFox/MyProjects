import pygame 
import sys
import random
import math

pygame.init()

width,height = 700,350
FPS = 60
clock = pygame.time.Clock()
score = 0

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (128,0,128)
gray = (192,192,192)
yellow = (255,255,0)



window = pygame.display.set_mode((width,height))

pygame.display.set_caption('Remember cards')
window.fill('white')
orginal_colors = [yellow,black,red,blue,green,purple]
circle_radius = 50
circle_pairs = orginal_colors*2
random.shuffle(circle_pairs)
original_circles_pos = []
for i in range(6):
    for j in range(2):
        center_x = ((width / 6) * (i + 1)) - (width / 12)
        center_y = ((height / 3) * (j + 1)) - (height / 6) + 50
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
for i in range(len(circle_pairs)):
    pos = original_circles_pos[i]
    col = gray
    pygame.draw.circle(window,col,pos,circle_radius)

pygame.display.update()
uncovered_circles = []
last_uncovered_circle = None

while True:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = i.pos
            for i in range(len(original_circles_pos)):
                print(i)
                circle_pos = circles_pos[i]
                distance = (math.fabs((mouse_pos[0] - circle_pos[0]) ** 2 + (mouse_pos[1] - circle_pos[1]) ** 2)) ** 0.5
                print(distance)
                if distance < circle_radius:
                    print('uraaaaa')


    clock.tick(FPS)
    pygame.display.update()