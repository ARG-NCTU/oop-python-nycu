import pygame
import pygame.joystick
import sys
import os
import time
from script.entity import physics_entity
from script.utils import load_image
from script.utils import load_tile
from script.tilemap import Tilemap

#constants
SCREEN_Width = 640
SCREEN_HEIGHT = 480
HALF_SCREEN_WIDTH = SCREEN_Width // 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
FPS = 60

class main_game:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

        pygame.display.set_caption("Koakuma's Adventure")
        self.screen = pygame.display.set_mode((SCREEN_Width, SCREEN_HEIGHT))
        #放大兩倍
        self.display = pygame.Surface((HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()

        self.player = physics_entity(self, "player", (100,100), (8,15))

        self.movements = [False,False]

        self.assets = {
            "decor" : load_tile("tiles/decor"),
            "stone" : load_tile("tiles/stone"),
            "grass" : load_tile("tiles/grass"),
            "large_decor" : load_tile("tiles/large_decor"),
            "player": load_image("entities/player.png")
        }

        self.tilemap = Tilemap(self)

        self.camera = [0,0] #camera position = offset of everything


    def run(self):
        while True:
            self.display.fill((14,219,248))

            self.camera[0] += (self.player.rect().centerx - self.display.get_width()/2 -self.camera[0])/20 #camera follow player x
            self.camera[1] += (self.player.rect().centery - self.display.get_height()/2 - self.camera[1])/20 #camera follow player y
            render_camera = [int(self.camera[0]), int(self.camera[1])]

            self.tilemap.render(self.display,offset=render_camera) #render background

            self.player.update((self.movements[1] - self.movements[0],0),self.tilemap) #update player
            self.player.render(self.display,offset=render_camera) #render player


            self.max_jump_height = -3  # Maximum jump velocity
            self.min_jump_height = -1   # Minimum jump velocity
            self.jump_start_time = None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movements[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movements[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movements[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movements[1] = False

                #joystick control
                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == 0:
                        if event.value < -0.5:
                            self.movements[0] = True
                        elif event.value > 0.5:
                            self.movements[1] = True
                        else:
                            self.movements[0] = False
                            self.movements[1] = False

                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        self.player.velocity[1] = -3


            self.screen.blit(pygame.transform.scale(self.display, (SCREEN_Width, SCREEN_HEIGHT)), (0,0))
            pygame.display.update()
            self.clock.tick(FPS)

main_game().run()
