import pygame

class physics_entity:
    def __init__(self,main_game,entity_type,position,size):
        self.main_game = main_game
        self.entity_type = entity_type
        self.position = list(position)  
        self.size = size
        self.velocity = [0,0]

    def update(self, movement=(0,0)):
        frame_movement = [movement[0] + self.velocity[0], movement[1] + self.velocity[1]]

        self.position[0] += frame_movement[0]
        self.position[1] += frame_movement[1]

    def render(self,surface):
        surface.blit(self.main_game.assets['player'],self.position)