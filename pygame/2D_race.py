import pygame
import sys
pygame.init()

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

window = pygame.display.set_mode(resolution)
pygame.display.set_caption('2D Race')

background = pygame.transform.scale(pygame.image.load('pygame/race/background.jpg'),resolution)
sprite1 = pygame.transform.scale(pygame.image.load('pygame/race/sprite1.png'),(100,75))
sprite2 = pygame.transform.scale(pygame.image.load('pygame/race/sprite2.png'),(100,75))
x1 = 250
y1 = 70
x2 = 250
y2 = 360
speed = 1

text = pygame.font.Font(None,60)
text_rendered1 = text.render('Player 1 wins!',True,(255,0,0))
text_rendered2 = text.render('Player 2 wins!',True,(255,0,0))

while True:
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))
    for i in pygame.event.get():  
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keyboard = pygame.key.get_pressed()
    if keyboard[pygame.K_a]:
        x1-=speed
    if keyboard[pygame.K_d]:
        x1+=speed
    if keyboard[pygame.K_LEFT]:
        x2-=speed
    if keyboard[pygame.K_RIGHT]:
        x2+=speed
    if x1 > 450:
        window.blit(text_rendered1, (100,225))
    if x2 > 450:
        window.blit(text_rendered2, (100,225))
    print(x1,x2)



    clock.tick(FPS)
    pygame.display.update()



