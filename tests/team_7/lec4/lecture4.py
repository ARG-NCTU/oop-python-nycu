'''
    This is a simple program that demonstrates the use of inheritance in Python.
    It also show the use of pygame library to draw shapes on the screen.
'''
# step 1: Import the required libraries
import pygame
import sys

# step 2: Define the Class you want to use in your program

class Shape:
    ### Please Implement your Shape class code here. ###
    def __init__(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
    
    def getCenterX(self):
        return self.center_x
    
    def getCenterY(self):
        return self.center_y
    
    def resetCenterPoint(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
    


class Rectangle(Shape):
    def __init__(self, center_x, center_y, width, height):
        super().__init__(center_x, center_y)
        self.width = width
        self.height = height

    #width:int
    #height:int

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def vertex_positions(self):
        half_width = self.width / 2
        half_height = self.height / 2
        return [
            (self.center_x - half_width, self.center_y - half_height),
            (self.center_x + half_width, self.center_y - half_height),
            (self.center_x + half_width, self.center_y + half_height),
            (self.center_x - half_width, self.center_y + half_height)
        ]

    def move(self, dx, dy):
        self.center_x += dx
        self.center_y += dy

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, (self.center_x - self.width // 2, self.center_y - self.height // 2, self.width, self.height))

class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        super().__init__(center_x, center_y)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def vertex_positions(self):
        return [(self.center_x, self.center_y)]

    def move(self, dx, dy):
        self.center_x += dx
        self.center_y += dy

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.center_x, self.center_y), self.radius)

class RegularTriangle(Shape):
    def __init__(self, center_x, center_y, side):
        super().__init__(center_x, center_y)
        self.side = side

    def area(self):
        return (math.sqrt(3) / 4) * self.side ** 2

    def perimeter(self):
        return 3 * self.side

    def vertex_positions(self):
        height = self.side * (3 ** 0.5) / 2
        half_side = self.side / 2
        return [
            (self.center_x - half_side, self.center_y + height / 3),
            (self.center_x + half_side, self.center_y + height / 3),
            (self.center_x, self.center_y - 2 * height / 3)
        ]

    def move(self, dx, dy):
        self.center_x += dx
        self.center_y += dy

    def draw(self, screen, color):
        height = self.side * (3 ** 0.5) / 2
        half_side = self.side / 2
        points = [
            (self.center_x - half_side, self.center_y + height / 3),
            (self.center_x + half_side, self.center_y + height / 3),
            (self.center_x, self.center_y - 2 * height / 3)
        ]
        pygame.draw.polygon(screen, color, points)


#### DO NOT MODIFY THE CODE BELOW THIS LINE ####

# step 3: Create the main function to run the program

## parameters for the main function
running = True
screen_width, screen_height = 800, 600
background_color = (255, 255, 255)
shape_color = (0, 0, 0)

## pygame initialization
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Lab 07 Demo 1")

shape_choice = 0
display_shape = [Rectangle(400, 300, 100, 200), Circle(400, 300, 100), RegularTriangle(400, 300, 100)]

## main loop
while running:
    screen.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            shape_choice = (shape_choice + 1) % 3
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                display_shape[shape_choice].move(-10, 0)
            elif event.key == pygame.K_RIGHT:
                display_shape[shape_choice].move(10, 0)
            elif event.key == pygame.K_UP:
                display_shape[shape_choice].move(0, -10)
            elif event.key == pygame.K_DOWN:
                display_shape[shape_choice].move(0, 10)
    display_shape[shape_choice].draw(screen, shape_color)
    pygame.display.flip()

pygame.quit()
sys.exit()