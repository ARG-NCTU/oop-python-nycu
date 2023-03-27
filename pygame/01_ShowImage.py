import pygame

# define param
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('01_ShowImage')

#load images
load_background = pygame.image.load('./img/sea.jpg').convert_alpha() 
load_img = pygame.image.load('./img/duckie.png').convert_alpha() 

#resize image
width = load_img.get_width()
height = load_img.get_height()
image_resize = pygame.transform.scale(load_img, (width * 0.15, height * 0.15))

#game loop
is_runnung = True
while is_runnung:
    screen.blit(load_background, (0, 0))
    screen.blit(image_resize, (300, 200))
    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            is_runnung = False
    pygame.display.update()
pygame.quit()