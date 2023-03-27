import pygame

#define param 
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('00_EmptyWindow')

#game loop
is_runnung = True
while is_runnung:
    screen.fill((255, 255, 255))
    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            is_runnung = False
    pygame.display.update()
pygame.quit()