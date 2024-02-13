import pygame
import sys
from math import pi
FPS = 60
clock = pygame.time.Clock()

pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption('FPS 60')

# pygame.draw.rect(window,(255,255,0),(10,10,50,200),10)
pygame.display.flip()
# pygame.draw.line(window,(0,255,255),(250,250),(300,300),10)
# pygame.draw.aaline(window,(0,255,255),(250,250),(300,300),10)
# pygame.draw.lines(window,(0,255,255),True,[(10,400),(2,300),(20,200)],2)
# pygame.draw.aalines(window,(0,255,255),True,[(100,400),(20,300),(200,200)])
# pygame.draw.polygon(window,(255,0,255),[(100,200),(200,300),(100,300),(400,400)])
# pygame.draw.circle(window,(100,255,50),(250,250),150,5,True,True)
# pygame.draw.ellipse(window,(100,255,50),(10,10,300,200))
# pygame.draw.arc(window,(255,0,0),(10,10,300,200),6,4,3)

# pygame.draw.circle(window,'red',(200,250),50)
# pygame.draw.circle(window,'blue',(300,250),50)

# polygon1 = pygame.Surface((104, 154))

# pygame.draw.polygon(polygon1,'white',[(52,152),(2,77),(52,2),(102,77)],5)

# rotated_polygon = pygame.transform.rotate(polygon1, 57)
# rotated_polygon2 = pygame.transform.rotate(polygon1, -57)
# window.blit(rotated_polygon2, (95, 205))
# window.blit(rotated_polygon, (220, 205))


# pygame.draw.polygon(window,'white',[(250,250),(200,175),(250,100),(300,175)],5)
# pygame.draw.line(window,'white',(250,249),(200,249),4)
# pygame.draw.line(window,'white',(250,249),(215,330),4)
# pygame.display.flip()



# 