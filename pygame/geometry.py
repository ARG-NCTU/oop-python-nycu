import pygame
import pyivp

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('pyivp Geometry Demo')

pattern = pyivp.string2SegList("format=lawnmower, x=200, y=200, height=200, width=200, lane_width=40,\
                                rows=north-south, startx=0, starty=0, degs=0")
waypoint_ploy = pyivp.string2Poly("x=600, y=200, format=radial, radius=100, pts=8")
waypoint_seg = waypoint_ploy.exportSegList(500, 200)

run = True
while run:

    screen.fill((202, 228, 241))

    for i in range(pattern.size()-1):
        x1 = int(pattern.get_vx(i))
        y1 = int(pattern.get_vy(i))
        x2 = int(pattern.get_vx(i+1))
        y2 = int(pattern.get_vy(i+1))
        pygame.draw.line(screen, (100,100,100), (x1, y1), (x2, y2))
    
    for i in range(waypoint_seg.size()):
        x1 = round(waypoint_seg.get_vx(i))
        y1 = round(waypoint_seg.get_vy(i))
        x2 = round(waypoint_seg.get_vx(i+1))
        y2 = round(waypoint_seg.get_vy(i+1))
        if i == waypoint_seg.size()-1:
            x2 = round(waypoint_seg.get_vx(0))
            y2 = round(waypoint_seg.get_vy(0))
        pygame.draw.line(screen, (100,100,100), (x1, y1), (x2, y2))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()