import pygame
import sys
import random

pygame.init()

resolution = (700,500)
FPS = 60
clock = pygame.time.Clock()
size_x = 50
size_y = 50
score = 0

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

window = pygame.display.set_mode(resolution)

pygame.display.set_caption('Ball.io')
food_radius = 20
def spawn_food():
    return random.randint(food_radius,resolution[0]-food_radius-100),random.randint(food_radius,resolution[1]-food_radius-100)

player_radius = 50

player_x = resolution[0]//2
player_y = resolution[1]//2
food_x = spawn_food()[0]
food_y= spawn_food()[1]

text = pygame.font.Font(None,60)
text_rendered1 = text.render(f'Score: {score}',True,(0,0,255))


while True:
    
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    mouse_x,mouse_y = pygame.mouse.get_pos()
    dx = mouse_x-player_x
    dy = mouse_y-player_y
    player_x+=dx*0.1
    player_y+=dy*0.1

    window.fill('black')
    window.blit(text_rendered1,(0,0))
    pygame.draw.circle(window,red,(food_x,food_y),food_radius)
    pygame.draw.circle(window,green,(int(player_x),int(player_y)),player_radius)
    
    distance = ((player_x - food_x) ** 2 + (player_y - food_y) ** 2) ** 0.5
    text_rendered1 = text.render(f'Score: {score}',True,(0,0,255))
    if distance<player_radius+food_radius:
        food_x = spawn_food()[0]
        food_y= spawn_food()[1]
        score+=1
        player_radius+=5
    
    
    pygame.display.update()
    clock.tick(FPS)
    