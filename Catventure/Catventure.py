import pygame
import random
import sys
import math
from constants import *

pygame.init()
pygame.display.set_caption(game_name)

game_window = pygame.display.set_mode((window_width, window_height))
font = pygame.font.SysFont("arialblack", 35)

def play(): 
    player_image = pygame.image.load("images/cat.png").convert_alpha()
    player_image = pygame.transform.scale(player_image, (player_width, player_height))
    player_image_walk = pygame.image.load("images/cat_walk.png").convert_alpha()
    player_image_walk = pygame.transform.scale(player_image_walk, (player_width*2, player_height))
    player_image_jump = pygame.image.load("images/cat_jump.png").convert_alpha()
    player_image_jump = pygame.transform.scale(player_image_jump, (player_width, player_height))
    star_image = pygame.image.load("images/can.png").convert_alpha()
    star_image = pygame.transform.scale(star_image, (star_width, star_height))
    shield_image = pygame.image.load("images/shield.png").convert_alpha()
    shield_image = pygame.transform.scale(shield_image, (star_width, star_height))
    potion_image = pygame.image.load("images/potion.png").convert_alpha()
    potion_image = pygame.transform.scale(potion_image, (star_width, star_height))
    fire_image = pygame.image.load("images/fire.png").convert_alpha()
    fire_image = pygame.transform.scale(fire_image, (star_width, star_height))
    enemy1_image = pygame.image.load("images/enemy1.png").convert_alpha()
    enemy1_image = pygame.transform.scale(enemy1_image, (enemy_width, enemy_height))
    enemy2_image = pygame.image.load("images/enemy2.png").convert_alpha()
    enemy2_image = pygame.transform.scale(enemy2_image, (enemy_width, enemy_height))
    bullet_image = pygame.image.load("images/bullet.png").convert_alpha()
    background_image = pygame.image.load("images/background.png").convert()
    background_image = pygame.transform.scale(background_image, (window_width, window_height))
    platform_image = pygame.image.load("images/platform.png").convert_alpha()
    arrow_image = pygame.image.load("images/arrow.png").convert_alpha()
    saw_image = pygame.image.load("images/saw.png").convert_alpha()
    saw_image = pygame.transform.scale(saw_image, (saw_width, saw_height))
    dart_image = pygame.image.load("images/dart.png").convert_alpha()
    dart_image = pygame.transform.scale(dart_image, (dart_width, dart_height))
    bullet_sound = pygame.mixer.Sound("sounds/bullet_sound.mp3")
    bullet_sound.set_volume(0.5)
    harm_sound = pygame.mixer.Sound("sounds/harm_sound.mp3")
    harm_sound.set_volume(0.5)
    get_star_sound = pygame.mixer.Sound("sounds/get_star_sound.mp3")
    get_star_sound.set_volume(0.5)
    shield_sound = pygame.mixer.Sound("sounds/shield_sound.mp3")
    shield_sound.set_volume(0.5)
    potion_sound = pygame.mixer.Sound("sounds/potion_sound.mp3")
    potion_sound.set_volume(0.5)
    resist_sound = pygame.mixer.Sound("sounds/resist_sound.mp3")
    resist_sound.set_volume(0.5)
    fire_sound = pygame.mixer.Sound("sounds/fire_sound.mp3")
    fire_sound.set_volume(0.5)
    
    class GameObject(pygame.sprite.Sprite):
        def __init__(self, x, y, image):
            pygame.sprite.Sprite.__init__(self)
            self.x = x
            self.y = y
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def rect_update(self):
            self.rect.x = self.x
            self.rect.y = self.y
            
        def draw(self):
            game_window.blit(self.image, (self.x, self.y))

    class Player(GameObject):  
        def __init__(self, x, y, image):
            super().__init__(x, y, image)
            self.vel_y = 0
            self.health = max_health
            self.fire_delay = 0
            self.down = False
            self.down_start_time = 0
            self.jumped = False
            self.can_jump = True
            self.current_animation = 'idle'
            self.current_frame = 0
            self.last_frame_update = 0
            self.invincible = False
            self.scattering = False
            self.inv_start_time = 0
            self.sct_start_time = 0
            self.animations = {
                'idle': [player_image], 
                'walk_left': create_animation(player_image_walk, player_width, player_height),
                'walk_right': create_animation(pygame.transform.flip(player_image_walk, True, False), player_width, player_height),
                'jump': [player_image_jump],
                'jump_right': [pygame.transform.flip(player_image_jump, True, False)]
            }

        def animate(self, current_time):
            animation = self.animations[self.current_animation]

            if current_time > self.last_frame_update + animation_interval:
                self.current_frame += 1
                if self.current_frame >= len(animation):
                    self.current_frame = 0
                self.image = animation[self.current_frame]
                self.last_frame_update = current_time

        def move_left(self):
            self.x -= player_speed
            self.current_animation = 'walk_left'

        def move_right(self):
            self.x += player_speed
            self.current_animation = 'walk_right'
            
        def jump(self):
            self.vel_y = -jump_speed
            self.jumped = True
            self.can_jump = False
        
        def shoot(self):
            self.fire_delay = fire_delay
            mouse_x, mouse_y = pygame.mouse.get_pos()
            direction = math.atan2(mouse_y - self.y, mouse_x - self.x)
            if self.scattering:
                angle_increment = math.radians(40) / num_bullets  # 計算角度間隔
                for i in range(num_bullets):
                    bullet_angle = direction + (i - (num_bullets // 2)) * angle_increment  # 計算子彈的發射角度
                    bullet = Bullet(self.x, self.y, bullet_image, bullet_angle)
                    bullets.add(bullet)
            else:
                bullet = Bullet(player.x, player.y, bullet_image, direction)
                bullets.add(bullet)

        def collide_platform(self):
            self.rect_update()
            for platform in  pygame.sprite.spritecollide(self, platforms, False, collided = None):
                if self.y <= platform.y - platform_height and self.vel_y > 0 and not self.down:
                    self.y = platform.rect.top - player_height
                    self.vel_y = 0
                    self.jumped = False
                    self.can_jump = True
        
        def check_harm(self):
            if self.invincible:
                resist_sound.play()
            else:
                self.health -= 1
                harm_sound.play()
              
        def harmed(self):
            for enemy in pygame.sprite.spritecollide(self, enemies, True, collided = None):
                self.check_harm()
            for arrow in pygame.sprite.spritecollide(self, arrows, True, collided = None):
                self.check_harm()   
            for saw in pygame.sprite.spritecollide(self, saws, True, collided = None):
                self.check_harm()
            for dart in pygame.sprite.spritecollide(self, darts, True, collided = None):
                self.check_harm()

        def boundary(self):
            if self.x < 0:
                self.x = 0
            elif self.x > window_width - player_width:
                self.x = window_width - player_width
            if self.y < 0:
                self.y = 0
                self.vel_y = 0
            elif self.y > window_height - floor_height:
                self.y = window_height - floor_height
                self.can_jump = True

        def update(self):
            self.harmed()
            self.current_animation = 'idle'
            x_move = 0
            y_move = 0

            key = pygame.key.get_pressed()
                    
            #Right
            if key[pygame.K_d]:
                self.move_right()
            #Left
            if key[pygame.K_a]:
                self.move_left()
            #Fall
            if key[pygame.K_s]:
                self.down_start_time = pygame.time.get_ticks()
                self.down = True
            elif not key[pygame.K_s] and pygame.time.get_ticks() - self.down_start_time > 150:
                self.down = False
            #Jump
            if key[pygame.K_SPACE]:
                self.current_animation = 'jump'
                if key[pygame.K_d]:
                    self.current_animation = 'jump_right'
                if self.jumped is False and self.can_jump:
                    self.jump()
            if not key[pygame.K_SPACE]:
                self.jumped = False
            #Shoot
            if pygame.mouse.get_pressed()[0] and self.fire_delay <= 0:
                self.shoot()
            if self.fire_delay > 0:
                self.fire_delay -= 1

            self.collide_platform()

            #Gravity
            self.vel_y += 1.2
            y_move += self.vel_y

            self.x += x_move
            self.y += y_move

            self.boundary()
            self.animate(pygame.time.get_ticks())
  
    class Bullet(GameObject):
        def __init__(self, x, y, image, direction):
            super().__init__(x, y, image)
            self.speed = bullet_speed
            self.direction = direction

        def move(self):
            dx = math.cos(self.direction) * self.speed
            dy = math.sin(self.direction) * self.speed
            self.x += dx
            self.y += dy
            
        def boundary(self):
            self.rect.x = self.x
            self.rect.y = self.y
            if self.rect.left > window_width or self.rect.right < 0 or self.rect.top > window_height or self.rect.bottom < 0:
                bullets.remove(self)
            
        def update(self):
            self.rect_update()
            self.move()
            self.boundary()
        
    class Enemy1(GameObject):
        def __init__(self, x, y, image):
            super().__init__(x, y, image)
            self.speed = enemy_speed

        def chase(self):
            if self.x < player.x:
                self.x += self.speed
            else:
                self.x -= self.speed

            if self.y < player.y:
                self.y += self.speed
            else:
                self.y -= self.speed
                            
        def update(self):
            self.rect_update()
            self.chase()
    
    class Enemy2(GameObject):
        def __init__(self, x, y, image):
            super().__init__(x, y, image)
            self.speed_x = enemy_speed
            self.speed_y = enemy_speed
            
        def chase(self):
            if self.x <= 0 or self.x >= window_width - enemy_width:
                self.speed_x = -self.speed_x
                self.x = max(0 , min(self.x, window_width - enemy_width))
            if self.y <= 0 or self.y >= window_height - enemy_height:
                self.speed_y = -self.speed_y
                self.y = max(0, min(self.y, window_height - enemy_height))
            self.x += self.speed_x
            self.y += self.speed_y
            
        def update(self):
            self.rect_update()
            self.chase()

    class Arrow(GameObject):
        def __init__(self, x, y, image):
            super().__init__(x, y, image)
            self.speed = arrow_speed
        
        def move_down(self):
            self.y += self.speed

        def boundary(self):
            if self.rect.top > window_height:
                arrows.remove(self)
            
        def update(self):
            self.rect_update()
            self.move_down()
            self.boundary()

    class Saw(GameObject):
        def __init__(self, x, y, image, speed):
            super().__init__(x, y, image)
            self.speed = speed
            self.current_animation = 'idle'
            self.current_frame = 0
            self.last_frame_update = 0
            self.animation = create_animation(saw_image, saw_width, saw_height)

        def move_horiz(self):
            self.x += self.speed
        
        def boundary(self):
            if self.x + saw_width > window_width:
                self.speed *= -1
                self.x = window_width - saw_width
            if self.x < 0:
                self.speed *= -1
                self.x = 0
               
        def animate(self, current_time):
            if current_time > self.last_frame_update + 150:
                self.current_frame += 1
                if self.current_frame >= len(self.animation):
                    self.current_frame = 0
                self.image = self.animation[self.current_frame]
                self.last_frame_update = current_time
                
        def update(self):
            self.rect_update()
            self.move_horiz()
            self.boundary()
            self.animate(pygame.time.get_ticks())

    class Dart(GameObject):
        def __init__(self, x, y, image, speed):
            super().__init__(x, y, image)
            self.speed_x = speed
            self.speed_y = 1.5
            
        def chase(self):
            if self.x <= 0 or self.x >= window_width - dart_width:
                self.speed_x = -self.speed_x
                self.x = max(0 , min(self.x, window_width - dart_width))
            if self.y <= 0 or self.y >= window_height - dart_height:
                self.speed_y = -self.speed_y
                self.y = max(0, min(self.y, window_height - dart_height))
            self.x += self.speed_x
            self.y += self.speed_y
            
        def update(self):
            self.rect_update()
            self.chase()
            
    class Platform(GameObject):
        def __init__(self, x, y, image, speed):
            super().__init__(x, y, image)
            self.speed = speed

        def move_horiz(self):
            self.x += self.speed
        
        def boundary(self):
            if self.x + platform_width > window_width:
                self.speed *= -1
                self.x = window_width - platform_width
            if self.x < 0:
                self.speed *= -1
                self.x = 0
        def update(self):
            self.rect_update()
            self.move_horiz()
            self.boundary()
            
    def create_animation(image, width, height):
        frames = []
        for i in range(image.get_width() // width):
            rect = pygame.Rect(i * width, 0, width, height)
            frames.append(image.subsurface(rect))
        return frames

    platforms = pygame.sprite.Group(
        Platform(500, 120, platform_image, -3),
        Platform(500, 380, platform_image, 3),
        Platform(200, 250, platform_image, 0),
        Platform(800, 250, platform_image, 0),
        Platform(200, 500, platform_image, 0),
        Platform(800, 500, platform_image, 0)
    )

    player = Player(600, 200, player_image)
    star = GameObject(random.randint(star_x_min, star_x_max), random.randint(star_y_min, star_y_max), star_image)
    
    shields = pygame.sprite.Group()
    potions = pygame.sprite.Group()
    fires = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    arrows = pygame.sprite.Group()
    saws = pygame.sprite.Group()
    darts = pygame.sprite.Group()

    def decrease_interval_by_time(interval):
        rate = decrease_interval_rate
        rand = random.randint(1,rate)
        if rand % rate == 0:
            interval -= 100
        min_interval = min_decrease_interval
        if interval < min_interval:
            interval = min_interval
        return interval

    #Arrow Event
    ARROW_EVENT = pygame.USEREVENT + 1
    ARROW_TIME = arrow_time
    pygame.time.set_timer(ARROW_EVENT, ARROW_TIME)
    def gen_arrow():
        arrow = Arrow(random.randint(0, window_width), 0, arrow_image)
        arrows.add(arrow)

    #Saw Event
    SAW_EVENT = pygame.USEREVENT + 2
    SAW_TIME = saw_time
    pygame.time.set_timer(SAW_EVENT, SAW_TIME)
    def gen_saw():
        saw = Saw(random.randint(0, window_width), window_height - saw_height - 60, saw_image, random.choice([-3, 3]))
        saws.add(saw)
        
    DART_EVENT = pygame.USEREVENT + 3
    DART_TIME = dart_time
    pygame.time.set_timer(DART_EVENT, DART_TIME)
    def gen_dart():
        dart = Dart(random.randint(0, window_width), 10, dart_image, random.choice([-5, 5]))
        darts.add(dart)

    clock = pygame.time.Clock()
    score = 0
    start_time = pygame.time.get_ticks()
    #Game Loop
    while True:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ARROW_EVENT:
                gen_arrow()
                ARROW_TIME = decrease_interval_by_time(ARROW_TIME)
                pygame.time.set_timer(ARROW_EVENT, ARROW_TIME)
            if event.type == SAW_EVENT and score >= 5:
                gen_saw()
                SAW_TIME = decrease_interval_by_time(SAW_TIME)
                pygame.time.set_timer(SAW_EVENT, SAW_TIME)
            if event.type == DART_EVENT and score >= 10:
                gen_dart()
                DART_TIME = decrease_interval_by_time(DART_TIME)
                pygame.time.set_timer(DART_EVENT, DART_TIME)

        if pygame.sprite.collide_rect(star, player):
            get_star_sound.play()
            score += 1
            star = GameObject(random.randint(star_x_min, star_x_max), random.randint(star_y_min, star_y_max), star_image)
            if len(enemies) < 5:
                if len(enemies) % 2:
                    enemy = Enemy1(random.randint(window_width-100, window_width-enemy_width), random.randint(0, window_height-enemy_height), enemy1_image)
                    enemies.add(enemy)
                else:
                    enemy = Enemy2(random.randint(0, 100), random.randint(0, window_height-enemy_height), enemy2_image)
                    enemies.add(enemy)
        #Create items
        if random.randint(1, shield_gen) == 1:
            shield = GameObject(random.randint(star_x_min, star_x_max), random.randint(star_y_min, star_y_max), shield_image)
            shields.add(shield)
        if random.randint(1, potion_gen) == 1:
            potion = GameObject(random.randint(star_x_min, star_x_max), random.randint(star_y_min, star_y_max), potion_image)
            potions.add(potion)
        if random.randint(1, fire_gen) == 1:
            fire = GameObject(random.randint(star_x_min, star_x_max), random.randint(star_y_min, star_y_max), fire_image)
            fires.add(fire)
        #Item collide
        for shield in pygame.sprite.spritecollide(player, shields, True, collided = None):
            player.invincible = True
            player.inv_start_time = pygame.time.get_ticks()
            shield_sound.play()
        if pygame.time.get_ticks() - player.inv_start_time >= invincible_last_time:
            player.invincible = False
        
        for potion in pygame.sprite.spritecollide(player, potions, True, collided = None):
            if player.health < 3:   
                player.health += 1
            potion_sound.play()

        for fire in pygame.sprite.spritecollide(player, fires, True, collided = None):
            player.scattering = True
            player.sct_start_time = pygame.time.get_ticks()
            fire_sound.play()
        if pygame.time.get_ticks() - player.sct_start_time >= scattering_last_time:
            player.scattering = False
        
        if pygame.sprite.groupcollide(bullets, enemies, True, True, collided = None) or\
        pygame.sprite.groupcollide(bullets, arrows, True, True, collided = None) or\
        pygame.sprite.groupcollide(bullets, saws, True, True, collided = None) or\
        pygame.sprite.groupcollide(bullets, darts, True, True, collided = None):
            bullet_sound.play()
        
        if player.health <= 0:
            return score, pygame.time.get_ticks() - start_time
        
        player.update()
        bullets.update()
        arrows.update()
        saws.update()
        darts.update()
        enemies.update()
        platforms.update()

        game_window.blit(background_image, (0, 0))
        platforms.draw(game_window)
        enemies.draw(game_window)
        arrows.draw(game_window)
        saws.draw(game_window)
        darts.draw(game_window)
        bullets.draw(game_window)
        star.draw()
        shields.draw(game_window)
        potions.draw(game_window)
        fires.draw(game_window)
        player.draw()
        if player.invincible:
            pygame.draw.circle(game_window, red, (player.x + player_width//2, player.y-10), 7)
        
        health_text = font.render("Health: " + str(player.health), True, red)
        game_window.blit(health_text, (window_width - health_text.get_width() - 10, 10))

        score_text = font.render("Score: " + str(score), True, black)
        game_window.blit(score_text, (10, 10))

        pygame.display.update()

button_start = pygame.Rect(350, 100, 500, 200)
button_exit = pygame.Rect(350, 400, 500, 200)
background_image = pygame.image.load("images/menu_bg.png").convert()
background_image = pygame.transform.scale(background_image, (window_width, window_height))
menu_text = "START"
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_over = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if button_start.collidepoint(event.pos):
                score, time = play()
                file_path = "records.txt"
                with open(file_path, "a") as file:
                    file.write(f"{score} {time/1000:.1f}\n")
                game_over = True
                menu_text = "AGAIN"
            if button_exit.collidepoint(event.pos):
                pygame.quit()
                sys.exit             

    game_window.blit(background_image, (0, 0))
    if game_over:
        game_window.blit(pygame.font.SysFont("arialblack", 80).render(f"Score: {score}", True, "white"), (400, 100))
        game_window.blit(pygame.font.SysFont("arialblack", 80).render(f"Time: {time/1000:.1f}s", True, "white"), (360, 250))
        game_window.blit(pygame.font.SysFont("arialblack", 70).render("Press space to continue!", True, "white"), (80, 400))
    else:
        pygame.draw.rect(game_window, "white", button_start)
        game_window.blit(pygame.font.SysFont("arialblack", 100).render(menu_text, True, "black"), (410, 120))
        pygame.draw.rect(game_window, "white", button_exit)
        game_window.blit(pygame.font.SysFont("arialblack", 100).render("QUIT", True, "black"), (450, 420))
    pygame.display.flip()