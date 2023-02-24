import pygame
from math import cos, sin, radians
import time
import itertools

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 960

t = 0
clock = pygame.time.Clock()
max_msl = 100
ship_loc = {'x':480, 'y':50}
msl_loc = ((300,600), (500,500), (700,600), (500,300))
msl_f = [[False]*max_msl,[False]*max_msl,[False]*max_msl,[False]*max_msl]
msl_x = [[0]*max_msl,[0]*max_msl,[0]*max_msl,[0]*max_msl]
msl_y = [[0]*max_msl,[0]*max_msl,[0]*max_msl,[0]*max_msl]
msl_a = [[0]*max_msl,[0]*max_msl,[0]*max_msl,[0]*max_msl]
no = [0]*4

def set_msl(mslNum,x,y):
    global no

    for a in range(100, 460, 10):
        msl_f[mslNum][no[mslNum]] = True
        msl_x[mslNum][no[mslNum]] = x
        msl_y[mslNum][no[mslNum]] = y
        msl_a[mslNum][no[mslNum]] = a
        no[mslNum] = (no[mslNum]+1)%max_msl

def move_msl(screen):
    for mslNum in range(4):
        for i in range(max_msl):
            if msl_f[mslNum][i] is True:
                msl_x[mslNum][i] = msl_x[mslNum][i] + 2*cos(radians(msl_a[mslNum][i]))
                msl_y[mslNum][i] = msl_y[mslNum][i] + 2*sin(radians(msl_a[mslNum][i]))
                pygame.draw.circle(screen, (255, 200, 0), (msl_x[mslNum][i], msl_y[mslNum][i]), 4)
                # print(f'draw{mslNum} {i},x = {msl_x[mslNum][i]}, y = {msl_y[mslNum][i]}')
            if msl_y[mslNum][i] < 10 or msl_y[mslNum][i] > 710 or msl_x[mslNum][i] < 10 or msl_x[mslNum][i] > 950 :
                msl_f[mslNum][i] = False

def collision():
    global t
    flat_x = list(itertools.chain(*msl_x))
    flat_y = list(itertools.chain(*msl_y))

    for x, y in list(zip(flat_x, flat_y)):
        # print(x,y,ship_loc['x'],ship_loc['y'])
        if (int(x)-6 <= int(ship_loc['x']) <= int(x)+6) and (int(y)-6 <= int(ship_loc['y']) <= int(y)+6): 
            t = pygame.time.get_ticks() 
            return True
    return False
    

def check_reset_msl(mslNum):
    
    global no
    if not any(msl_f[mslNum]):
        from random import randint
        randomX = randint(20, 940)
        randomY = randint(20, 700)
        set_msl(mslNum, x=randomX, y=randomY)
        no = [0]*4


def move_ship(screen,key):
    global ship_loc
    
    if key[pygame.K_UP] == 1:
        ship_loc['y'] = ship_loc['y']-3
    if key[pygame.K_DOWN] == 1:
        ship_loc['y'] = ship_loc['y']+3
    if key[pygame.K_LEFT] == 1:
        ship_loc['x'] = ship_loc['x']-3
    if key[pygame.K_RIGHT] == 1:
        ship_loc['x'] = ship_loc['x']+3
    

set_msl(mslNum=0, x=msl_loc[0][0], y=msl_loc[0][1])
set_msl(mslNum=1, x=msl_loc[1][0], y=msl_loc[1][1])
set_msl(mslNum=2, x=msl_loc[2][0], y=msl_loc[2][1])
set_msl(mslNum=3, x=msl_loc[3][0], y=msl_loc[3][1])

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


run = True
pause = False
while run:
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (ship_loc['x'], ship_loc['y']), 10)
    key = pygame.key.get_pressed()
    move_ship(screen, key)
    move_msl(screen)
    
    pause = collision()
    
    while pause:
        font = pygame.font.SysFont(None, 50)
        
        img = font.render(str(int(t/1000)), True, (255, 255, 255))
        screen.blit(img, (40, 40))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pause = False

    for i in range(4):
        check_reset_msl(i)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(60)
    pygame.display.flip()
    pygame.display.update()

pygame.quit()