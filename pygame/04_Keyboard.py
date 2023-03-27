import pygame
import random

# define param
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 30

class Keyboard():
    def __init__(self, image, scale=0.01):
        width = image.get_width()
        height = image.get_height()
        MAX_WIDTH = SCREEN_WIDTH - width * scale
        MAX_HEIGHT = SCREEN_HEIGHT - height * scale
        self.image = pygame.transform.scale(image, 
                                            (int(width * scale), 
                                            int(height * scale)))
        self.dotX = random.randrange(MAX_WIDTH)
        self.dotY = random.randrange(MAX_HEIGHT)

    def draw(self, surface):
        surface.blit(self.image, (self.dotX , self.dotY))
        
    def move(self, N_PIXELS_TO_MOVE=5):
        if event.key == pygame.K_LEFT:
            self.dotX -= N_PIXELS_TO_MOVE 
            print('left')
        elif event.key == pygame.K_RIGHT:
            self.dotX += N_PIXELS_TO_MOVE 
            print('right')
        elif event.key == pygame.K_UP:
            self.dotY -= N_PIXELS_TO_MOVE 
            print('up')
        elif event.key == pygame.K_DOWN:
            self.dotY += N_PIXELS_TO_MOVE 
            print('down')
        if (self.dotX > 640) or (self.dotX < 0) or \
            (self.dotY > 480) or (self.dotY < 0):
            self.dotX = 300 
            self.dotY = 200 
            print('@@@ out of range @@@')
        
    
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('03_Keyboard')

#load image
dot = pygame.image.load('./img/dot.png')
start_keyboard= Keyboard(dot, 0.01)

#game loop
is_runnung = True
while is_runnung: 
    screen.fill((0, 0, 0))  
    start_keyboard.draw(screen)
    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            is_runnung = False
        if event.type == pygame.KEYDOWN:  
            start_keyboard.move(10)
            
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)

pygame.quit()