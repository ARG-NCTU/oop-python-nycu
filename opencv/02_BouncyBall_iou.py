import pygame
import cv2 as cv
import numpy as np
from random import choice

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

import numpy as np

def calculate_iou(circle1, circle2):
    iou=0
    # Calculate the distance between the centers of the circles
    
    # Calculate the radius of the intersection between the circles
    
    # Calculate the area of the intersection and union between the circles
    
    # Calculate the IOU as the ratio between the area of the intersection and the area of the union
    
    # Check if the circles overlap
    
    return iou

class Ball():
    def __init__(self):
        self.radius = 40
        self.x = np.random.randint(self.radius, SCREEN_WIDTH-self.radius)
        self.y = np.random.randint(self.radius, SCREEN_HEIGHT-self.radius)
        self.x_direction = choice((-2, 2))
        self.y_direction = choice((-2, 2))

    def move(self):
        self.x += self.x_direction*2
        self.y += self.y_direction*2
        self.contact_detect()

    def contact_detect(self):
        if self.x + self.radius >= SCREEN_WIDTH or\
                self.x - self.radius <= 0:
            self.x_direction = -self.x_direction

        if self.y + self.radius >= SCREEN_HEIGHT or\
                self.y - self.radius <= 0:
            self.y_direction = -self.y_direction

    def draw(self, screen):
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.radius)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('BouncyBall')
ball = Ball()
ball_2 = Ball()

# game loop
is_running = True
while is_running:
    screen.fill(WHITE)
    ball.move()
    ball.draw(screen)
    ball_2.move()
    ball_2.draw(screen)

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()
    # Convert the Pygame surface to a numpy array
    screen_array = pygame.surfarray.array3d(screen)
    # Convert the RGB surface array to a BGR image array for OpenCV
    image_array = np.flip(screen_array, axis=2)
    gray = cv.cvtColor(image_array, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 3, rows / 8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=50)
    if circles is not None:
        if circles.shape[1] is 2:
            iou = calculate_iou(circles[0][0], circles[0][1])
            if iou > 0:
                print(iou)

    clock.tick(30)
pygame.quit()
