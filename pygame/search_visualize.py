import random
import pygame
import argparse
import numpy as np
import sys
sys.path.append('../utils')
from search import GridProblem, line, random_lines, astar_search, path_states

DISPLAY_BACKGROUND = (250, 250, 250)
DISPLAY_OBSTACLE   = (150, 150, 150)
DISPLAY_PATH       = (0, 0, 255)
DISPLAY_SEACHED    = (205, 205, 10)
DISPLAY_START      = (255, 0, 0)
DISPLAY_GOAL       = (50, 205, 50)

DISPLAY_MAP = {
    0: DISPLAY_BACKGROUND,
}
'''
coordinate rule:

    Y
    ^
    +
    +
    O + + > X

'''

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--display_px', default = 1000, type = int, help = 'pixel size about display window')
    parser.add_argument('--env_size', default = 200, type = int, help = 'number of the side length of gird map')
    parser.add_argument('--initial_position', default = (-50, -50), type = int, nargs = '+', help = 'coordinate = [x, y], the place we start searching')
    parser.add_argument('--goal_position', default = (80, 30), type = int, nargs = '+', help = 'coordinate = [x, y], the destination')
    parser.add_argument('--fps', default = 180, type = int, help = 'frame per second for display update usage')
    args = parser.parse_args()
    return args

class Visualize():
    def __init__(self, args):
        self.cfg = args
        self.clock = pygame.time.Clock()
        self.fps = self.cfg.fps
        self.env_grid_px_per_cell = self.cfg.display_px / self.cfg.env_size

    def trans_to_dispaly(self, standard_x, standard_y):
        pygame_x = round(standard_x*self.env_grid_px_per_cell + self.cfg.display_px/2)
        pygame_y = round(self.cfg.display_px/2 - standard_y*self.env_grid_px_per_cell)
        transfer_tuple = (pygame_x, pygame_y)
        return transfer_tuple

    def display_init(self):
        pygame.init()
        pygame.display.init()
        screen = pygame.display.set_mode([self.cfg.display_px, self.cfg.display_px])
        screen.fill(DISPLAY_BACKGROUND)
        return screen

    def render_background(self, screen):
        self.clock.tick(self.fps)
        screen.fill(DISPLAY_BACKGROUND)
        return

    def render_obstacles(self, screen, obstacles):
        for obstacle in obstacles:
            (x,y)=self.trans_to_dispaly(obstacle[0], obstacle[1])
            pygame.draw.rect(
                screen, 
                DISPLAY_OBSTACLE, 
                pygame.Rect(x, y, 10, 10)
            )
        return

    def render_path(self, screen, path):
        for point in path:
            (x,y)=self.trans_to_dispaly(point[0], point[1])
            pygame.draw.rect(
                screen, 
                DISPLAY_PATH, 
                pygame.Rect(x, y, 10, 10)
            )
        return

    def render_searched(self, screen, searched):
        for point in searched:
            (x,y)=self.trans_to_dispaly(point[0], point[1])
            pygame.draw.rect(
                screen, 
                DISPLAY_SEACHED, 
                pygame.Rect(x, y, 10, 10)
            )
        return
    
    def render_point(self, screen, point, color):
        (x,y)=self.trans_to_dispaly(point[0], point[1])
        pygame.draw.rect(
            screen, 
            color, 
            pygame.Rect(x, y, 10, 10)
        )
        return

    def render_update(self):
        pygame.display.flip()
        return

    def close(self):
        pygame.display.quit()
        pygame.quit()
        return

def grid_problem_init(args):
    # grid problem init
    frame = line(-100, 50, 0, -1, 100) | line(-50, 100, 1, 0, 100) | line(100, 50, 0, -1, 100)
    cup = line(60, 44, -1, 0, 15) | line(60, 20, -1, 0, 20) | line(60, 44, 0, -1, 24)

    # choose the map we want to test

    # single obstacle map
    d1 = GridProblem(
        initial=args.initial_position, 
        goal=args.goal_position, 
        obstacles=random_lines(X=range(-80,80), Y=range(-80,80), N=300) | frame
    )

    # cup type obstacle map
    d2 = GridProblem(
        initial=args.initial_position, 
        goal=args.goal_position, 
        obstacles=cup | frame | line(0, 35, 0, -1, 10) | line(20, 37, 0, -1, 17) | line(40, 31, 0, -1, 19)
    )
    
    return d2


def plot_search(args, display, grid_map):
    # display setting
    screen = display.display_init()
    solution, reached = astar_search(grid_map, return_search_history=True)
    path = path_states(solution)
    visited = []

    while True:
        for point in reached:
            visited.append(point)
            display.render_background(screen)
            display.render_searched(screen, visited)
            display.render_obstacles(screen, grid_map.obstacles)
            display.render_point(screen, point, DISPLAY_PATH)
            display.render_point(screen, grid_map.initial, DISPLAY_START)
            display.render_point(screen, grid_map.goal, DISPLAY_GOAL)
            display.render_update()
        
        for i in range(args.fps * 5):
            display.render_background(screen)
            display.render_searched(screen, visited)
            display.render_obstacles(screen, grid_map.obstacles)
            display.render_path(screen, path)
            display.render_point(screen, grid_map.initial, DISPLAY_START)
            display.render_point(screen, grid_map.goal, DISPLAY_GOAL)
            display.render_update()
        
        visited = []
    display.close()
    return
 

# if __name__ == "__main__":

random.seed(42) # To make this reproducible

arg = parse_args()

display = Visualize(arg)

grid_map = grid_problem_init(arg)

plot_search(arg, display, grid_map)