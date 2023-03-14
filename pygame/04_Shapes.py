import pygame
import random
import math 

# define param
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 60

class Shape():
    def __init__(self,line_width):
        self.line_width = line_width
        self.X = random.randrange(SCREEN_WIDTH)
        self.Y = random.randrange(SCREEN_HEIGHT)

    def circle(self,screen):
        '''
        random (x, y) in __init__
        '''
        pygame.draw.circle(screen, (255,255,255), (self.X, self.Y), 30, self.line_width)

    def square(self,screen, step = 50):
        '''
        start point (x, y)  
        line length: step
        '''
        step = abs(step) 
        if ((self.X + step) < SCREEN_WIDTH and (self.X + step) > 0 and (self.Y +step) < SCREEN_HEIGHT and (self.Y +step) > 0):
            pygame.draw.line(screen, (255, 255, 255), (self.X, self.Y), (self.X + step, self.Y ), self.line_width)
            pygame.draw.line(screen, (255, 255, 255), (self.X, self.Y), (self.X, self.Y +step), self.line_width)
            pygame.draw.line(screen, (255, 255, 255), (self.X + step, self.Y), (self.X + step, self.Y + step), self.line_width)
            pygame.draw.line(screen, (255, 255, 255), (self.X, self.Y + step), (self.X + step, self.Y + step), self.line_width)
        else:
            print('@@@ out of range @@@')
            
    def polygon (self, screen, point_list):
        '''
        point_list: ((x1,y1), (x2,y2), (x3,y3), (x4,y4),...)
        '''
        pygame.draw.polygon(screen, (255, 255, 255), point_list)

    def arc(self,screen, rect = (50, 100, 200, 200), angle_start = 0, angle_stop = math.pi):
        '''
        rect : (point_x, point_y, diameter_x, diameter_y)
        angle_start (rad)
        angle_stop  (rad)
        '''
        pygame.draw.arc(screen, (255, 255, 255), rect, angle_start, angle_stop, self.line_width)
    

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('04_Shapes')

#game loop
run = True
while run: 
    draw_shape= Shape(1)
    screen.fill((0,0,0))  
    shape = str(input())

    if shape == 'circle':
        draw_shape.circle(screen)
    elif shape == 'square':
        draw_shape.square(screen, 100)  
    elif shape == 'polygon':
        draw_shape.polygon(screen,((100,100), (200,100), (250,200), (200,300), (100,300), (50,200)))  
    elif shape == 'arc':
        draw_shape.arc(screen, (50, 100, 200, 200), -math.pi, 0)    
    else: 
        pass

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
   
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)

pygame.quit()