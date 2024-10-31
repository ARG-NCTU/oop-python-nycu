import pygame
import sys
from script.entity import physics_entity
from script.utils import load_image

#constants
SCREEN_Width = 640
SCREEN_HEIGHT = 480
HALF_SCREEN_WIDTH = SCREEN_Width // 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
FPS = 60

class main_game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Koakuma's Adventure")
        self.screen = pygame.display.set_mode((SCREEN_Width, SCREEN_HEIGHT))
        #放大兩倍
        self.display = pygame.Surface((HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()

        self.player = physics_entity(self, "player", (100,200), (8,15))

        self.movements = [False,False]

        self.assets = {
            "player": load_image("entities/player.png")
        }

        self.collision_area = pygame.Rect(50,50,300,400)
    def run(self):
        while True:
            self.display.fill((14,219,248))

            self.player.update((self.movements[1] - self.movements[0],0))
            self.player.render(self.display)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movements[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movements[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movements[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movements[1] = False


            self.screen.blit(pygame.transform.scale(self.display, (SCREEN_Width, SCREEN_HEIGHT)), (0,0))
            pygame.display.update()
            self.clock.tick(FPS)

main_game().run()