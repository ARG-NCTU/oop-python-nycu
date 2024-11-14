import pygame
import pygame.joystick
import sys
import os
import random
import math
from script.entity import physics_entity, Player, Enemy
from script.utils import load_image
from script.utils import load_tile
from script.utils import load_images
from script.utils import Animation
from script.tilemap import Tilemap, small_tile
from script.particle import Particle
from script.spark import Spark

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

        self.movements = [False,False]

        self.assets = {
            "decor" : load_tile("tiles/decor"),
            "stone" : load_tile("tiles/stone"),
            "grass" : load_tile("tiles/grass"),
            "large_decor" : load_tile("tiles/large_decor"),
            "player": load_image("entities/player.png"),
            "background": load_image("background.png"),
            "enemy/idle" : Animation(load_images("entities/enemy/idle"),duration=6,loop=True),
            "enemy/run" : Animation(load_images("entities/enemy/run"),duration=4,loop=True),
            "player/idle" : Animation(load_images("entities/player/idle"),duration=6,loop=True),
            "player/run" : Animation(load_images("entities/player/run"),duration=4,loop=True),
            "player/jump" : Animation(load_images("entities/player/jump"),duration=5,loop=True),
            "player/slide" : Animation(load_images("entities/player/slide"),duration=5,loop=True),
            "player/wall_slide" : Animation(load_images("entities/player/wall_slide"),duration=5,loop=True),
            "particle/leaf" : Animation(load_images("particles/leaf"),duration=20,loop=False),
            "particle/particle" : Animation(load_images("particles/particle"),duration=6,loop=False),
            "gun" : load_image("gun.png"),
            "projectile" : load_image("projectile.png"),

        }
        self.load_level()

    def load_level(self):

        self.player = Player(self, (100,100), (8,15) , HP = 5)

        self.tilemap = Tilemap(self)

        self.projectiles = []
        self.particles = []
        self.sparks = []

        self.camera = [0,0] #camera position = offset of everything
        self.dead = 0 #dead animation

        self.tilemap.load("tests/group1/game_testing/tilemap.pickle")

        self.leaf_spawners = []

        for tree in self.tilemap.extract([('large_decor',2)],keep=True):
            self.leaf_spawners.append(pygame.Rect(4+tree.pos[0], 4+tree.pos[1], 23, 13))

        self.enemy_spawners = []
        for spawner in self.tilemap.extract([('spawners',0),('spawners',1)],keep=False):
            if spawner.variant == 0:
                self.player.position = spawner.pos #player start position
            else:
                self.enemy_spawners.append(Enemy(self,spawner.pos,(8,15)))
             
        

    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0,0))

            if self.dead > 0:
                self.dead += 1
                if self.dead > 40:
                    self.load_level()

            self.camera[0] += (self.player.rect().centerx - self.display.get_width()/2 -self.camera[0])/20 #camera follow player x
            #self.camera[1] += (self.player.rect().centery - self.display.get_height()/2 - self.camera[1])/20 #camera follow player y
            render_camera = [int(self.camera[0]), int(self.camera[1])]

            for spawner in self.leaf_spawners:
                if random.random() * 49999 < spawner.width* spawner.height:
                    pos = (spawner.x + random.random()*spawner.width, spawner.y + random.random()*spawner.height)
                    self.particles.append(Particle(self,'leaf',pos,velocity=[-0.1,0.3],frame=random.randint(0,20)))
            self.tilemap.render(self.display,offset=render_camera) #render background

            for enemy in self.enemy_spawners.copy():
                kill = enemy.update((0,0),self.tilemap)
                enemy.render(self.display,offset=render_camera)
                if kill:
                    self.enemy_spawners.remove(enemy)
            if not self.dead:
                self.player.update((self.movements[1] - self.movements[0],0),self.tilemap) #update player
                self.player.render(self.display,offset=render_camera) #render player


            self.max_jump_height = -3  # Maximum jump velocity
            self.min_jump_height = -1   # Minimum jump velocity
            self.jump_start_time = None

            #[[x,y],direction,timer]
            for projectile in self.projectiles.copy():
                projectile[0][0] += projectile[1]
                projectile[2] += 1
                img = self.assets['projectile']
                self.display.blit(img,(projectile[0][0]-img.get_width()/2 -render_camera[0],projectile[0][1]-img.get_height()/2-render_camera[1]))
                if self.tilemap.solid_check(projectile[0]):
                    self.projectiles.remove(projectile) 
                    for i in range(4):
                        self.sparks.append(Spark(projectile[0],random.random()*math.pi*2,2+random.random()))
                elif projectile[2] > 360:
                    self.projectiles.remove(projectile)
                elif abs(self.player.dashing) < 50:
                    if self.player.rect().collidepoint(projectile[0]):
                        self.projectiles.remove(projectile)
                        for i in range(30):
                            angle = random.random()*math.pi*2
                            speed = random.random() *5
                            self.sparks.append(Spark(self.player.rect().center,angle,2+random.random()))  
                            self.particles.append(Particle(self,'particle',self.player.rect().center,[math.cos(angle+math.pi)*speed*0.5,math.sin(angle+math.pi)*speed*0.5],frame=random.randint(0,7)))  
                        self.player.HP -= 1
                        if self.player.HP <= 0:
                            self.dead += 1                  
            for spark in self.sparks.copy():
                kill = spark.update()
                spark.render(self.display,offset=render_camera)
                if kill:
                    self.sparks.remove(spark)   

            for particle in self.particles.copy():
                kill = particle.update()
                if particle.p_type == 'leaf':
                    particle.pos[0] += math.sin(particle.animation.frame*0.035)*0.3
                particle.render(self.display,offset=render_camera)
                if kill:
                    self.particles.remove(particle)

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
                        self.player.jump()
                    if event.key == pygame.K_SPACE:
                        self.player.dash()
                    if event.key == pygame.K_z: 
                        self.player.attack()
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
                        self.player.jump()
                    if event.button == 7:
                        self.player.dash()
                    if event.button == 3:
                        self.player.attack()


            self.screen.blit(pygame.transform.scale(self.display, (SCREEN_Width, SCREEN_HEIGHT)), (0,0))
            pygame.display.update()
            self.clock.tick(FPS)

main_game().run()
