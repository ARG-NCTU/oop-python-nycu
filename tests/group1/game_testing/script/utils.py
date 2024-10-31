import pygame

BASE_IMAGE_PATH = "tests/group1/game_testing/data/images/"

def load_image(path):
    img = pygame.image.load(BASE_IMAGE_PATH + path).convert()
    img.set_colorkey((0,0,0))
    return img