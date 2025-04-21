import pygame
import random
import math



class BouncyBall:
    def __init__(self, screen, color, radius, pos, velocity):
        self.screen = screen
        self.color = color
        self.radius = radius
        self.pos = pos
        self.velocity = velocity
    def update_ball(self,ball, screen_width, screen_height):
    # 更新位置
        ball['pos'][0] += ball['velocity'][0]
        ball['pos'][1] += ball['velocity'][1]

    # 檢查左右邊界，若碰到則反轉 x 軸速度
        if ball['pos'][0] - ball['radius'] <= 0 or ball['pos'][0] + ball['radius'] >= screen_width:
            ball['velocity'][0] = -ball['velocity'][0]

    # 檢查上下邊界，若碰到則反轉 y 軸速度
        if ball['pos'][1] - ball['radius'] <= 0 or ball['pos'][1] + ball['radius'] >= screen_height:
            ball['velocity'][1] = -ball['velocity'][1]

    def draw_ball(self,ball):
        pygame.draw.circle(ball['screen'], ball['color'], (int(ball['pos'][0]), int(ball['pos'][1])), ball['radius'])
    # add your code here
    

def main():
    # add your code here
    pygame.init()
    screen_width = 640
    screen_height =480

    screen=pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("BouncyBall")

    ball1 = {
        'screen': screen,
        'color': (255, 255, 255),       
        'radius': 20,
        'pos': [screen_width // 2, screen_height // 2],  # 初始位置在畫面中央
        'velocity': [3, 3]              
    }
    ball2 = {
        'screen': screen,
        'color': (200, 200, 100),       
        'radius': 10,
        'pos': [screen_width // 3, screen_height // 3],  # 初始位置在畫面中央
        'velocity': [10, 20]              
    }

    b1=BouncyBall(ball1['screen'], ball1['color'], ball1['pos'], ball1['radius'], ball1['velocity'])
    b2=BouncyBall(ball2['screen'], ball2['color'], ball2['pos'], ball2['radius'], ball2['velocity'])

    clock = pygame.time.Clock()
    running = True

    # 主迴圈：持續更新與繪製
    while running:
        screen.fill((0, 0, 0))  # 清空畫面，填充黑色背景
        clock.tick(60)
       
        # 處理事件，當使用者關閉視窗時結束程式
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        b1.update_ball(ball1, screen_width, screen_height)
        b1.draw_ball(ball1)   
        b2.update_ball(ball2,screen_width, screen_height)
        b2.draw_ball(ball2)        
        pygame.display.update()

    # add your code here  
   
    # 更新球的位置及反彈邏輯
    
        # add your code here
    

    # add your code here
    pygame.quit()

if __name__ == "__main__":
    main()