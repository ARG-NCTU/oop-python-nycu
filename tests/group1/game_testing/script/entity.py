import pygame
from script.particle import Particle
from script.spark import Spark
import math
import random

class physics_entity:
    def __init__(self,main_game,entity_type,position,size):
        self.main_game = main_game
        self.entity_type = entity_type
        self.position = list(position)  
        self.size = size
        self.velocity = [0,0]
        self.dashing = 0

        #Animation
        self.action = ''
        self.anim_offset = (-3,-3) #避免動畫比原本圖片大所以預留空間
        self.flip = False
        self.set_action('idle')

    def set_action(self,action):
        if self.action != action:
            self.action = action
            self.anim = self.main_game.assets[self.entity_type + "/" + action].copy()

    def rect(self):
        return pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def update(self, movement=(0,0),tilemap=None):
        self.check_collision = {'up':False, 'down':False, 'left':False, 'right':False}
        frame_movement = [movement[0] + self.velocity[0], movement[1] + self.velocity[1]]

        self.position[0] += frame_movement[0]
        entity_rect = self.rect()

        for rect in tilemap.tile_collision(self.position):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.check_collision['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.check_collision['left'] = True
                self.position[0] = entity_rect.x

        if movement[0] > 0:
            self.flip = False
        if movement[0] < 0:
            self.flip = True

        self.position[1] += frame_movement[1]
        entity_rect = self.rect()

        for rect in tilemap.tile_collision(self.position):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.check_collision['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.check_collision['up'] = True
                self.position[1] = entity_rect.y

        self.velocity[1] = min(5,self.velocity[1]+0.1) #gravity

        if self.check_collision['down'] or self.check_collision['up']:
            self.velocity[1] = 0      

        self.anim.update()  

    def render(self,surface,offset=[0,0]):
        surface.blit(pygame.transform.flip(self.anim.img(),self.flip,False),(self.position[0]-offset[0]+self.anim_offset[0],self.position[1]-offset[1]+self.anim_offset[1]))
        #surface.blit(self.main_game.assets['player'],(self.position[0]-offset[0],self.position[1]-offset[1])    )

class Player(physics_entity):
    def __init__(self,main_game,position,size):     
        super().__init__(main_game,'player',position,size)
        self.air_time = 0
        self.jump_count = 2

    def update(self, movement=(0,0),tilemap=None):
        super().update(movement,tilemap)
        #if player is dashing, do not apply gravity
        if abs(self.dashing) > 50:
            self.velocity[1] = 0
        self.air_time += 1
        if self.check_collision['down']:
            self.air_time = 0
            self.jump_count = 2
        if self.air_time > 4:
            self.set_action('jump') 
        elif movement[0] != 0:
            self.set_action('run')
        else:
            self.set_action('idle')

        if self.dashing > 0:
            self.dashing = max(0,self.dashing-1)
        if self.dashing < 0:
            self.dashing = min(0,self.dashing+1)
        if abs(self.dashing) > 50:
            self.velocity[0] = abs(self.dashing) / self.dashing * 8
            if abs(self.dashing) == 51:
                self.velocity[0] *= 0.1
            pv = [math.cos(random.random()*math.pi*2)*random.random()*0.5+0.5,math.sin(random.random()*math.pi*2)*random.random()*0.5+0.5]
            self.main_game.particles.append(Particle(self.main_game,'particle',self.rect().center,pv,frame=random.randint(0,7)))
        if self.velocity[0] > 0:
            self.velocity[0] = max(0,self.velocity[0]-0.1)
        if self.velocity[0] < 0:
            self.velocity[0] = min(0,self.velocity[0]+0.1)   

    def render(self,surface,offset=[0,0]):
        super().render(surface,offset)
        #surface.blit(self.main_game.assets['player'],(self.position[0]-offset[0],self.position[1]-offset[1])    )
    def jump(self):
        if self.jump_count > 0:
            self.velocity[1] = -3
            self.jump_count -= 1
            self.air_time = 5
            self.set_action('jump')

    def dash(self):
        if not self.dashing:
            self.dashing = -60 if self.flip else 60

    def render(self,surface,offset=[0,0]):
        if abs(self.dashing) <= 50:
            super().render(surface,offset)

class Enemy(physics_entity):
    def __init__(self,main_game,position,size):
        super().__init__(main_game,'enemy',position,size)
        self.flip = True
        self.set_action('idle')

        self.walking = 0

    def update(self, movement=(0,0),tilemap=None):
        if self.walking:
            movement = (movement[0] - 0.5 if self.flip else 0.5, movement[1])
            self.walking = max(0,self.walking-1)
            if not self.walking:
                distance = (self.main_game.player.rect().centerx - self.rect().centerx, self.main_game.player.rect().centery - self.rect().centery)
                if abs(distance[1]) < 16:
                    if(self.flip and distance[0] < 0): #player is to the left and enemy is facing left
                        self.main_game.projectiles.append([[self.rect().centerx-7,self.rect().centery],-1.5,0])
                        for i in range(4):
                            self.main_game.sparks.append(Spark(self.main_game.projectiles[-1][0],random.random()+math.pi-0.5,2+random.random()))
                    elif(not self.flip and distance[0] > 0): #player is to the right and enemy is facing right
                        self.main_game.projectiles.append([[self.rect().centerx+7,self.rect().centery],1.5,0])
                        for i in range(4):
                            self.main_game.sparks.append(Spark(self.main_game.projectiles[-1][0],random.random()-0.5,2+random.random()+2))
        elif random.random() < 0.01:
            self.walking = random.randint(30,120)
        if movement[0] > 0:
            self.set_action('run')
        else:
            self.set_action('idle') 
        super().update(movement,tilemap)

    def render(self,surface,offset=[0,0]):
        super().render(surface,offset)
        if self.flip:
            surface.blit(pygame.transform.flip(self.main_game.assets['gun'],True,False),(self.rect().centerx-4-self.main_game.assets['gun'].get_width() - offset[0],self.rect().centery - offset[1]))
        else:
            surface.blit(self.main_game.assets['gun'],(self.rect().centerx + 4 - offset[0],self.rect().centery - offset[1]))