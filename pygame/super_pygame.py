import pygame
import sys

pygame.mixer.init(frequency=90000,channels=20)


                                                                                                                                                                                                                    # print(pygame.font.get_fonts())

                                                                                                                                                                                                                    # text = pygame.font.Font(None,60)
                                                                                                                                                                                                                    # text_rendered = text.render('Hello world',True,(255,100,100))
pygame.mixer.music.load('pygame/images/sb_indreams.mp3')
vol = 0.1
print(pygame.mixer.music.get_volume())
pygame.mixer.music.set_volume(vol)
pygame.mixer.music.play(loops=0,start=0,fade_ms=3)
pause = False
stop = False

window = pygame.display.set_mode((500,500))
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                pause = not pause
                if pause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            if i.key == pygame.K_0:
                
                stop = not stop

                if stop == True:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play()
    keyboard = pygame.key.get_pressed()
    if keyboard[pygame.K_UP]:
        vol += 0.01
        pygame.mixer.music.set_volume(vol)
    if keyboard[pygame.K_DOWN]:
        vol -= 0.01
        pygame.mixer.music.set_volume(vol)
    









                                                                                                                                                                                                                                                                        # window.blit(text_rendered, (10,250))
    pygame.display.update()
    pygame.time.Clock().tick(60)


