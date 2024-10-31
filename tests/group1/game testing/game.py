import pygame
import sys

#constants
SCREEN_Width = 640
SCREEN_HEIGHT = 480

pygame.init()
pygame.display.set_caption("Koakuma's Adventure")
screen = pygame.display.set_mode((SCREEN_Width, SCREEN_HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)