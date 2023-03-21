import pygame
import random
import math 

# define param
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 60

class Shape():
    def __init__(self):
        self.line_width = 1
        self.X = random.randrange(SCREEN_WIDTH)
        self.Y = random.randrange(SCREEN_HEIGHT)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    def circle(self,screen, radius=10):
        '''
        random (x, y) in __init__
        '''
        pygame.draw.circle(screen, (255, 255, 255), (self.X, self.Y), radius, self.line_width)

    def square(self, screen, step=50):
        '''
        start point (x, y)  
        line length: step
        '''
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(30, 30, 60, 60),  2)
            
    def polygon (self, screen, point_list=((100, 100), (200, 100), (250, 200), (200, 300), (100, 300), (50, 200))):
        '''
        point_list: ((x1, y1), (x2, y2), (x3, y3), (x4, y4),...)
        '''
        pygame.draw.polygon(screen, (255, 255, 255), point_list)

    def arc(self, screen, rect=(300, 200, 50, 30), angle_start=0, angle_stop=math.pi):
        '''
        rect : (point_x, point_y, diameter_x, diameter_y)
        angle_start (rad)
        angle_stop  (rad)
        '''
        pygame.draw.arc(screen, (255, 255, 255), rect, angle_start, angle_stop, self.line_width)

    def decision(self, screen):
        '''
        To decide the output according to the input
        '''
        shape_list = [self.circle, self.square, self.polygon, self.arc]
        screen.fill((0, 0, 0)) 
        random.choice(shape_list)(screen)

        
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('04_Shapes')

screen.fill((0, 0, 0)) 
print('===== Press anykey to generate random shape. =====')

#game loop
is_runnung = True

while is_runnung: 
    draw_shape = Shape() 
    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            is_runnung = False
        if event.type == pygame.KEYDOWN:
            draw_shape.decision(screen)

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)

pygame.quit()