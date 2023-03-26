import pyivp
import pygame

class PyIvPGeometry:
    '''
    This class is used to calculate the area of a shape.
    '''

    PI = 3.141592653589793
    
    # a static method is a method that does not require an instance of the class
    # draw is a static method with decorator @staticmethod
    @staticmethod
    def draw(screen, shape):

        if isinstance(shape, pyivp.XYPolygon):
            for i in range(shape.size() - 1):
                x1 = int(shape.get_vx(i))
                y1 = int(shape.get_vy(i))
                x2 = int(shape.get_vx(i + 1))
                y2 = int(shape.get_vy(i + 1))
                pygame.draw.line(screen, (100, 100, 100), (x1, y1), (x2, y2))

        elif isinstance(shape, pyivp.XYSegList):
            for i in range(shape.size()):
                x1 = round(shape.get_vx(i))
                y1 = round(shape.get_vy(i))
                x2 = round(shape.get_vx(i + 1))
                y2 = round(shape.get_vy(i + 1))
                if i == shape.size()- 1:
                    x2 = round(shape.get_vx(0))
                    y2 = round(shape.get_vy(0))
                pygame.draw.line(screen, (100, 100, 100), (x1, y1), (x2, y2))
        else:
            raise ValueError(f"No such shape found: '{shape}'. \
                             Supported shapes are 'XYPolygon', 'XYSegList'.")
