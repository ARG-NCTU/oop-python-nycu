import pygame
import pyivp

import sys
import os

# Get the absolute path of the upper-level directory
upper_level_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the upper-level directory to sys.path
sys.path.append(upper_level_path)

from utils.pyivp_pygame_draw import PyIvPGeometry

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('pyivp Geometry Demo')

pattern_block = pyivp.string_to_seglist(" format=lawnmower, x = 200, y = 200, height = 200, width = 200, lane_width = 40,\
                                rows = north - south, startx = 0, starty = 0, degs = 0 ")
waypoint_ploy = pyivp.string_to_poly("x = 600, y = 200, format = radial, radius = 100, pts = 8")
waypoint_seg = waypoint_ploy.export_seglist(500, 200)

is_runnung = True
while is_runnung:

    screen.fill((202, 228, 241))

    try:
        PyIvPGeometry.draw(screen, pattern_block)
        PyIvPGeometry.draw(screen, waypoint_seg)
    except ValueError as e:
        print(e)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_runnung = False

    pygame.display.update()

pygame.quit()
