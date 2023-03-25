import pygame
import gymnasium as gym
import time
import random
import matplotlib.pyplot as plt
import numpy as np
import math
import csv




DISPLAY_WATER = (14, 180, 255)
DISPLAY_LAND = (160, 60, 10)

DISPLAY_MAP = {
    0: DISPLAY_WATER,
    1: DISPLAY_LAND,
}


class EmptyEnv(gym.Env):
    def __init__(self, args):
        self.cfg = args

        self.clock = pygame.time.Clock()
        self.fps = self.cfg.fps

        self.display_map = np.zeros((self.cfg.env_dim[1], self.cfg.env_dim[0], 3))

        for i in range(self.cfg.env_dim[0]):
                for j in range(self.cfg.env_dim[1]):
                    self.display_map[j][i] = DISPLAY_MAP[0]

        self.visited_waypoints = []


        # environment params
        self.env_grid_px_per_m = self.cfg.env_px / self.cfg.env_dim[0]




    def blit_rotate_img(self, surface, image, pos, angle, img_size):
        image_rect = image.get_rect(topleft = (pos[0] - img_size, pos[1] - img_size))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
        
        rotated_offset = offset_center_to_pivot.rotate(-angle)

        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

        rotated_image = pygame.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

        surface.blit(rotated_image, rotated_image_rect)
        return

    def trans_to_dispaly(self, standard_x, standard_y):
        pygame_x = round(self.cfg.env_px/2 - standard_y*self.env_grid_px_per_m)
        pygame_y = round(self.cfg.env_px/2 - standard_x*self.env_grid_px_per_m)
        transfer_tuple = (pygame_x, pygame_y)
        return transfer_tuple

    def distance(self, p1, p2):
        return math.sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))
        
    def display_init(self):
        pygame.init()
        pygame.display.init()
        screen = pygame.display.set_mode([self.cfg.env_px, self.cfg.env_px])
        return screen

    def character_init(self, img_name, img_px_size):
        character = pygame.image.load(img_name)
        character_resize = pygame.transform.scale(character, (img_px_size, img_px_size))
        return character_resize

    def render_background(self, screen):
        self.clock.tick(self.fps)
        env = pygame.Surface((self.cfg.env_dim[0], self.cfg.env_dim[1]))
        pygame.surfarray.blit_array(env, self.display_map)
        env = pygame.transform.scale(env, (self.cfg.env_px, self.cfg.env_px))
        screen.blit(env, (0, 0))
        return

    def render_path(self, screen, waypoint, current_frame=0):
        if current_frame < 0:
            return
        
        if len(waypoint[current_frame]) == 3:
            self.visited_waypoints.append(waypoint[current_frame])
            for waypoint[current_frame] in self.visited_waypoints:
                pygame.draw.circle(
                    screen, 
                    (250, 15, 30), 
                    self.trans_to_dispaly(
                        waypoint[current_frame][0],
                        waypoint[current_frame][1]
                    ), 
                    0.5 * self.env_grid_px_per_m
                )

    def render_character(self, screen, character, waypoint, current_frame=0):
        if current_frame < 0:
            return
        
        if len(waypoint[current_frame]) == 3:
            self.blit_rotate_img(
                screen, 
                character, 
                self.trans_to_dispaly(
                    waypoint[current_frame][0],
                    waypoint[current_frame][1]
                ),
                waypoint[current_frame][2],
                character.get_height()/2
            )
        else:
            for agent in range(self.cfg.usv_agent_num):
                self.blit_rotate_img(
                    screen, 
                    character, 
                    self.trans_to_dispaly(
                        self.observatiopn_space["pos"][agent][0],
                        self.observatiopn_space["pos"][agent][1]
                    ),
                    self.observatiopn_space["angle"][agent]
                )
        return

    def render_update(self):
        pygame.display.flip()
        return

    def close(self):
        pygame.display.quit()
        pygame.quit()
        return

    def clear_path(self):
        self.visited_waypoints = []
        return
