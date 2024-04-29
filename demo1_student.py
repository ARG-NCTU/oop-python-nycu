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
    def resetCenterpoint(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
    def area(self):
        pass
    def perimeter(self):
        pass
    def vertex_positions(self):
        pass
    def move(self, dx, dy):
        self.center_x += dx
        self.center_y += dy
    def draw(self,screen, color):
        pass


class Rectangle(Shape):
    ### Please Implement your Rectangle class code here. ###
    def __init__(self, center_x, center_y, width, height):
        super().__init__(center_x, center_y) 
        #super means the parent class also initialize the parent class
        self.width = width
        self.height = height

    def draw(self, screen, color):
        pygame.draw.polygon(screen, color, self.vertex_positions())

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def vertex_positions(self):
        return [(self.getCenterX() - self.width/2, self.getCenterY() - self.height/2),
                (self.getCenterX() + self.width/2, self.getCenterY() - self.height/2),
                (self.getCenterX() + self.width/2, self.getCenterY() + self.height/2),
                (self.getCenterX() - self.width/2, self.getCenterY() + self.height/2)]
    def move(self, dx, dy):
        super().move(dx, dy)
    

class Circle(Shape):
    ### Please Implement your Circle class code here. ###
    def __init__(self, center_x, center_y, radius):
        super().__init__(center_x, center_y)
        self.radius = radius

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.getCenterX(), self.getCenterY()), self.radius)

    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius
    def vertex_positions(self):
        return [(self.getCenterX() - self.radius, self.getCenterY() - self.radius),
                (self.getCenterX() + self.radius, self.getCenterY() - self.radius),
                (self.getCenterX() + self.radius, self.getCenterY() + self.radius),
                (self.getCenterX() - self.radius, self.getCenterY() + self.radius)]
    def move(self, dx, dy):
        super().move(dx, dy)
    

class RegularTriangle(Shape):
    ### Please Implement your RegularTriangle class code here. ###
    def __init__(self, center_x, center_y, side):
        super().__init__(center_x, center_y)
        self.side = side
    
    def draw(self, screen, color):
        pygame.draw.polygon(screen, color, self.vertex_positions())
    def area(self):
        return 0.5 * self.side * self.side * 3**0.5
    def perimeter(self):
        return 3 * self.side
    def vertex_positions(self):
        return [(self.getCenterX(), self.getCenterY() - self.side/2),
                (self.getCenterX() + self.side/2, self.getCenterY() + self.side/2),
                (self.getCenterX() - self.side/2, self.getCenterY() + self.side/2)]
    def move(self, dx, dy):
        super().move(dx, dy)

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
        elif event.type == pygame.MOUSEBUTTONDOWN: # change the shape
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