import pygame
from script.particle import Particle
from script.spark import Spark, Flame, Gold_Flame
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


        if self.check_collision['down'] or self.check_collision['up']:
            self.velocity[1] = 0      

        self.anim.update()  

    def render(self,surface,offset=[0,0]):
        surface.blit(pygame.transform.flip(self.anim.img(),self.flip,False),(self.position[0]-offset[0]+self.anim_offset[0],self.position[1]-offset[1]+self.anim_offset[1]))
        #surface.blit(self.main_game.assets['player'],(self.position[0]-offset[0],self.position[1]-offset[1])    )

class Player(physics_entity):
    def __init__(self,main_game,position,size,HP,weapon=None,spell_card=None,accessory=[]):     
        super().__init__(main_game,'player',position,size)
        self.air_time = 0
        self.jump_count = 2
        self.HP = HP
        self.attack_cool_down = 0    
        self.inv_time = 0
        self.extra_attack = False
        self.extra_attack_frame = 0
        self.max_inv_time = 60
        self.max_attack_cool_down = 30
        self.max_mana = 30
        self.mana = self.max_mana
        self.weapon = weapon.name if weapon else "none"
        self.spell_card = spell_card
        self.accessory = accessory
        self.damage=2
        if self.weapon == "貪欲的叉勺":
            self.damage = 3
            self.max_attack_cool_down = 20

        self.spell_card = spell_card.name if spell_card else "none"
        self.accessory = [accessory[i].name for i in range(len(accessory))]

        self.accessory = ["巫女的御幣"]

        if "水晶吊墜" in self.accessory:
            self.max_mana += 10
            self.mana = self.max_mana
        if "心型吊墜" in self.accessory:
            self.HP += 1
        if "亡靈提燈" in self.accessory:    
            self.inv_time += 30
        #"蝙蝠吊墜" setting in enemy
        if "銀製匕首" in self.accessory:
            self.damage += 1
        if "斷線的人偶" in self.accessory:
            pass
        if "神社的符咒" in self.accessory:  
            pass
        if "巫女的御幣" in self.accessory:
            self.extra_attack = True


    def update(self, movement=(0,0),tilemap=None):
        super().update(movement,tilemap)
        #if player is dashing, do not apply gravity
        if not (abs(self.dashing) > 50):
            self.velocity[1] = min(5,self.velocity[1]+0.1) #gravity
        self.air_time += 1

        self.attack_cool_down = max(0,self.attack_cool_down-1)
        self.inv_time = max(0,self.inv_time-1)
        if abs(self.dashing)<20:
            self.dashing = 0

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

        self.extra_attack_frame = max(0,self.extra_attack_frame-1)
        if self.extra_attack_frame == 1:
            temp=self.attack_cool_down
            self.attack_cool_down = 0
            self.attack(self.extra_attack)
            self.attack_cool_down = temp


    def render(self,surface,offset=[0,0]):
        super().render(surface,offset)
        #surface.blit(self.main_game.assets['player'],(self.position[0]-offset[0],self.position[1]-offset[1])    )
    def jump(self):
        if self.jump_count > 0:
            self.velocity[1] = -2.5
            self.jump_count -= 1
            self.air_time = 5
            self.set_action('jump')

    def attack(self,is_extra=False):
        if self.attack_cool_down == 0:
            self.attack_cool_down = self.max_attack_cool_down
            if self.weapon == "none":
                #attack a rect-space area in front of the player
                if self.flip:
                    hitbox = pygame.Rect(self.position[0]-36,self.position[1],28,16)
                else:
                    hitbox = pygame.Rect(self.position[0]+8,self.position[1],28,16)   
                for enemy in self.main_game.enemy_spawners:
                    if hitbox.colliderect(enemy.rect()):
                        enemy.HP -= self.damage
                        for i in range(30):
                            angle = random.random()*math.pi*2
                            speed = random.random() *5
                            self.main_game.sparks.append(Gold_Flame(enemy.rect().center,angle,2+random.random()))  
                            self.main_game.particles.append(Particle(self.main_game,'particle',enemy.rect().center,[math.cos(angle+math.pi)*speed*0.5,math.sin(angle+math.pi)*speed*0.5],frame=random.randint(0,7)))  
                        self.main_game.sparks.append(Gold_Flame(enemy.rect().center, 0, 5+random.random()))
                        self.main_game.sparks.append(Gold_Flame(enemy.rect().center, math.pi, 5+random.random()))
                if self.extra_attack and not is_extra:
                    self.extra_attack_frame = 11
            elif self.weapon == "貪欲的叉勺":
                if self.flip:
                    hitbox = pygame.Rect(self.position[0]-36,self.position[1],28,22)
                else:
                    hitbox = pygame.Rect(self.position[0]+8,self.position[1],28,22)   
                for enemy in self.main_game.enemy_spawners:
                    if hitbox.colliderect(enemy.rect()):
                        enemy.HP -= self.damage
                        for i in range(30):
                            angle = random.random()*math.pi*2
                            speed = random.random() *5
                            self.main_game.sparks.append(Gold_Flame(enemy.rect().center,angle,2+random.random()))  
                            self.main_game.particles.append(Particle(self.main_game,'particle',enemy.rect().center,[math.cos(angle+math.pi)*speed*0.5,math.sin(angle+math.pi)*speed*0.5],frame=random.randint(0,7)))  
                        self.main_game.sparks.append(Gold_Flame(enemy.rect().center, 0, 5+random.random()))
                        self.main_game.sparks.append(Gold_Flame(enemy.rect().center, math.pi, 5+random.random()))
                for bullet in self.main_game.projectiles:
                    if hitbox.colliderect(pygame.Rect(bullet[0][0]-4,bullet[0][1]-4,8,8)):
                        self.main_game.projectiles.remove(bullet)
                        for i in range(10):
                            angle = random.random()*math.pi*2
                            speed = random.random() *5
                            self.main_game.sparks.append(Spark(bullet[0],angle,2+random.random()))  
                if self.extra_attack and not is_extra:
                    self.extra_attack_frame = 11


    def dash(self):
        #set verticle velocity to 0
        if not self.dashing:
            self.velocity[1] = 0
            self.dashing = -60 if self.flip else 60
            self.inv_time = 15 #extra 5 frams of invincibility

    def take_damage(self,damage=1,relative_pos=[0,0]):
        if self.inv_time == 0:
            self.relative_pos = relative_pos
            if self.relative_pos[0] > 0:
                self.flip = True
                self.velocity[0] = 2
                self.velocity[1] = -2   
            else:
                self.flip = False
                self.velocity[0] = -2
                self.velocity[1] = -2
            #if player takes damage, lose 1 HP and got knockback to the opposite direction of the enemy
            self.HP -= damage
            self.inv_time = self.max_inv_time
            for i in range(30):
                angle = random.random()*math.pi*2
                speed = random.random() *5
                self.main_game.sparks.append(Spark(self.rect().center,angle,2+random.random()))  
                self.main_game.particles.append(Particle(self.main_game,'particle',self.rect().center,[math.cos(angle+math.pi)*speed*0.5,math.sin(angle+math.pi)*speed*0.5],frame=random.randint(0,7)))
            if self.HP <= 0:
                self.main_game.dead += 1    

    def render(self,surface,offset=[0,0]):
        if abs(self.dashing) <= 50:
            super().render(surface,offset)

class Enemy(physics_entity):
    def __init__(self,main_game,position,size,phase=1):
        super().__init__(main_game,'enemy',position,size)
        self.flip = True
        self.set_action('idle')

        self.phase = phase

        self.idle_time = 0 #time that enemy do nothing
        self.walking = 0
        self.jumping = False
        self.air_dashing = False
        self.time_counter = 0
        self.current_counter = 0
        self.attack_cool_down = 0
        if self.phase == 1:
            self.HP = 30
        elif self.phase == 2:
            self.HP = 25
        self.attack_combo = 0
        #combo 1: jump - dash - drop attack - land shot
        #combo 2: dash forward and shoot 3 bullets

    def update(self, movement=(0,0),tilemap=None):
        self.time_counter += 1
        if self.check_player_pos()[0] > 0:
            self.flip = False
        else:
            self.flip = True
        
        if self.phase == 1:
            self.attack_cool_down = max(0,self.attack_cool_down-1)
            if not (self.air_dashing):
                self.velocity[1] = min(7,self.velocity[1]+0.1) #gravity
            if self.walking and self.attack_combo == 0:
                self.idle_time = 0
                movement = (movement[0] - 0.5 if self.flip else 0.5, movement[1])
                self.walking = max(0,self.walking-1)
                if not self.walking:
                    self.normal_shoot()
            elif (random.random() < 0.02) and self.attack_combo == 0:
                self.idle_time = 0
                if random.choice([True,False]):
                    self.walking = random.randint(30,70)
                elif self.attack_cool_down == 0:
                    self.attack_combo = random.choice([1,2])
                    if self.attack_combo == 1:
                        self.jump()
                        self.attack_combo = 1
                        self.attack_cool_down = 300
                        self.current_counter = self.time_counter
                    elif self.attack_combo == 2:
                        self.dash()
                        self.attack_cool_down = 180
                        self.current_counter = self.time_counter
            else:
                self.idle_time += 1

            if self.idle_time > 150:
                self.idle_time = 0
                if random.choice([True,False]):
                    self.walking = random.randint(30,90)
                else:
                    self.jump()
                    self.attack_combo = 1
                    self.attack_cool_down = 300
                    self.current_counter = self.time_counter


            if self.attack_combo == 1: #jump - dash - drop attack - land shot
                if self.jumping and (self.time_counter-self.current_counter) > 30:
                    self.jumping = False
                    self.velocity = [0,0]
                    self.current_counter = self.time_counter
                    self.air_dash()
                elif self.air_dashing:
                    player_pos = self.check_player_pos()
                    if abs(player_pos[0]) < 8 or self.time_counter - self.current_counter >30:
                        self.air_dashing = False
                        self.velocity = [0,0]
                        self.current_counter = self.time_counter
                        self.drop_attack()
                #collide with ground
                elif self.check_collision['down'] and not self.jumping:
                    self.attack_combo = 0
                    self.current_counter = self.time_counter
                    self.land_shoot()
            elif self.attack_combo == 2: #dash forward and shoot 3 bullets
                if self.time_counter-self.current_counter == 10:
                    self.velocity[0] = 0
                    self.normal_shoot()
                elif self.time_counter-self.current_counter == 30:
                    self.normal_shoot()
                elif self.time_counter-self.current_counter == 50:
                    self.normal_shoot()
                elif self.time_counter-self.current_counter == 70:
                    self.normal_shoot()
                    self.attack_combo = 0
                    self.current_counter = 0


        #if player collides with enemy, player takes damage
        if self.rect().colliderect(self.main_game.player.rect()) and abs(self.main_game.player.dashing) < 50: 
            self.main_game.player.take_damage(1,self.check_player_pos())
        elif self.rect().colliderect(self.main_game.player.rect()) and abs(self.main_game.player.dashing) > 50 and "蝙蝠吊墜" in self.main_game.player.accessory:
            self.HP -= self.main_game.player.damage
            for i in range(30):
                angle = random.random()*math.pi*2
                speed = random.random() *5
                self.main_game.sparks.append(Gold_Flame(self.rect().center,angle,2+random.random()))  
                self.main_game.particles.append(Particle(self.main_game,'particle',self.rect().center,[math.cos(angle+math.pi)*speed*0.5,math.sin(angle+math.pi)*speed*0.5],frame=random.randint(0,7)))  
            if self.HP <= 0:
                return True


            

        if movement[0] > 0:
            self.set_action('run')
        else:
            self.set_action('idle') 

        if self.HP <= 0:
            return True
        super().update(movement,tilemap)

    def check_player_pos(self):
        return (self.main_game.player.rect().centerx - self.rect().centerx, self.main_game.player.rect().centery - self.rect().centery)

    def dash(self):
        #boss will move towards player's direction at a high speed for a short duration
        distance = self.check_player_pos()  
        if distance[0] > 0:
            self.velocity[0] = 5
        else:
            self.velocity[0] = -5
    def air_dash(self):
        #boss will move towards player's direction at a high speed for a short duration
        distance = self.check_player_pos()
        if distance[0] > 0:
            self.velocity[0] = 5
        else:
            self.velocity[0] = -5
        self.air_dashing = True
    def land_shoot(self):
        #boss will shoot five projectiole to the left, up left, up, up right, right
        self.main_game.projectiles.append([[self.rect().centerx-7,self.rect().centery],-1.5,0])
        self.main_game.projectiles.append([[self.rect().centerx-7,self.rect().centery-7],-1.5,-1.5])
        self.main_game.projectiles.append([[self.rect().centerx+7,self.rect().centery-7],1.5,1.5])
        self.main_game.projectiles.append([[self.rect().centerx+7,self.rect().centery],1.5,0])
        for i in range(30):
            angle = random.random()*math.pi*2
            speed = random.random() *3
            self.main_game.sparks.append(Flame(self.rect().center,angle,2+random.random()))  

    def normal_shoot(self):
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
            
                        
    def jump(self):
        #boss will jump and dash towards player's direction after a short delay
        self.velocity[1] = -4
        self.jumping = True
    def drop_attack(self):
        #boss will drop down and land, dealing damage to player if player is below
        self.velocity[1] = 7
        self.main_game.sparks.append(Spark(self.rect().center, 1.5*math.pi, 5+random.random()))

    def render(self,surface,offset=[0,0]):
        super().render(surface,offset)
        if self.flip:
            surface.blit(pygame.transform.flip(self.main_game.assets['gun'],True,False),(self.rect().centerx-4-self.main_game.assets['gun'].get_width() - offset[0],self.rect().centery - offset[1]))
        else:
            surface.blit(self.main_game.assets['gun'],(self.rect().centerx + 4 - offset[0],self.rect().centery - offset[1]))










class Boss(physics_entity):
    def __init__(self,main_game,position,size):
        super().__init__(main_game,"boss",position,size)
        self.HP = 10
        self.set_action('idle')
    def update(self, movement=(0,0),tilemap=None):
        super().update(movement,tilemap)
        pass
    def render(self,surface,offset=[0,0]):
        super().render(surface,offset)
    def dash(self):
        #boss will move towards player's direction at a high speed for a short duration
        distance = (self.main_game.player.rect().centerx - self.rect().centerx, self.main_game.player.rect().centery - self.rect().centery)
        if distance[0] > 0:
            self.velocity[0] = 5
        else:
            self.velocity[0] = -5
    def shoot(self):
        #boss will shoot a projectile towards player's direction
        distance = (self.main_game.player.rect().centerx - self.rect().centerx, self.main_game.player.rect().centery - self.rect().centery)
        if distance[0] > 0:
            self.main_game.projectiles.append([[self.rect().centerx+7,self.rect().centery],1.5,0])
        else:
            self.main_game.projectiles.append([[self.rect().centerx-7,self.rect().centery],-1.5,0])
        for i in range(4):
            self.main_game.sparks.append(Spark(self.main_game.projectiles[-1][0],random.random()-0.5,2+random.random()+2))
    def jump(self):
        #boss will jump and dash towards player's direction
        self.velocity[1] = -5
        self.set_action('jump')
        self.dash()
        self.drop_attack()
    def drop_attack(self):
        #boss will drop down and land, dealing damage to player if player is below
        self.velocity[1] = 5
        self.set_action('jump')
        #spark effect
        self.main_game.sparks.append(Spark(self.rect().center, 0, 5+random.random()))
        self.main_game.sparks.append(Spark(self.rect().center, math.pi, 5+random.random()))
        