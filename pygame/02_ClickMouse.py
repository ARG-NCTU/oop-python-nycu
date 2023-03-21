import pygame

# define param
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 20

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('02_ClickMouse')

#load image
dot = pygame.image.load('./img/dot.png').convert_alpha() 

#resize image
width = dot.get_width()
height = dot.get_height()
dot_resize = pygame.transform.scale(dot, (width * 0.01, height * 0.01))

#game loop
is_runnung = True
while is_runnung:
    screen.fill((0, 0, 0))

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            is_runnung = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouseX, mouseY = event.pos
            print(f'X:{mouseX}, Y:{mouseY}')
            screen.blit(dot_resize, (mouseX, mouseY))  

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
pygame.quit()