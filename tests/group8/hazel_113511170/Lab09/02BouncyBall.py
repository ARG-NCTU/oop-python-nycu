import pygame
import random
import math



class BouncyBall:
    def __init__(self, screen, color, pos,radius,  velocity):
        self.screen = screen
        self.color = color
        self.radius = radius
        self.pos = pos
        self.velocity = velocity
        self.mass= radius * 2  # 假設質量與半徑成正比
        self.elasticity = 0.8  # 彈性係數，0 < elasticity < 1，越接近1彈性越好   

    def collision(self, other_ball):      
        # 計算兩球心距離
        distance = math.sqrt((self.pos[0] - other_ball.pos[0]) ** 2 + (self.pos[1] - other_ball.pos[1]) ** 2)
        # 判斷是否碰撞
        if distance < self.radius + other_ball.radius:
            # 計算碰撞後的速度
            normal = [(other_ball.pos[0] - self.pos[0]) / distance, (other_ball.pos[1] - self.pos[1]) / distance]
            relative_velocity = [self.velocity[0] - other_ball.velocity[0], self.velocity[1] - other_ball.velocity[1]]
            velocity_along_normal = relative_velocity[0] * normal[0] + relative_velocity[1] * normal[1]

            if velocity_along_normal > 0:
                return

            restitution = min(self.elasticity, other_ball.elasticity)

            impulse_magnitude = -(1 + restitution) * velocity_along_normal / (1 / self.mass + 1 / other_ball.mass)

            self.velocity[0] += impulse_magnitude * normal[0] / self.mass
            self.velocity[1] += impulse_magnitude * normal[1] / self.mass

    def update_ball(self,other,ball, screen_width, screen_height):
    # 更新位置
        ball['pos'][0] += ball['velocity'][0]
        ball['pos'][1] += ball['velocity'][1]
        self.collision(other)

    # 檢查左右邊界，若碰到則反轉 x 軸速度
        if ball['pos'][0] - ball['radius'] <= 0 or ball['pos'][0] + ball['radius'] >= screen_width:
            ball['velocity'][0] = -ball['velocity'][0]

    # 檢查上下邊界，若碰到則反轉 y 軸速度
        if ball['pos'][1] - ball['radius'] <= 0 or ball['pos'][1] + ball['radius'] >= screen_height:
            ball['velocity'][1] = -ball['velocity'][1]


        
    #劃出球球
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
    
    #撞球桌圖片載入
    backrgound=pygame.image.load("shoot-ball.jpg").convert_alpha()
    backrgound=pygame.transform.scale(backrgound,(screen_width,screen_height))

    #隨機產生兩個球的初始位置
    x_axis=random.sample(range(0,screen_width),2)
    y_axis=random.sample(range(0,screen_height),2)

    ball1 = {
        'screen': screen,
        'color': (255, 255, 255),       
        'radius': 40,
        'pos': [x_axis[0], y_axis[0]], 
        'velocity': [3, 3]              
    }
    ball2 = {
        'screen': screen,
        'color': (150, 50, 200),       
        'radius': 60,
        'pos': [x_axis[1], y_axis[1]],  
        'velocity': [3, 5]              
    }

    b1=BouncyBall(ball1['screen'], ball1['color'], ball1['pos'], ball1['radius'], ball1['velocity'])
    b2=BouncyBall(ball2['screen'], ball2['color'], ball2['pos'], ball2['radius'], ball2['velocity'])

    clock = pygame.time.Clock()
    running = True

    # 主迴圈：持續更新與繪製
    while running:
        screen.fill((0, 0, 0))  # 清空畫面，填充黑色背景
        clock.tick(60)
        screen.blit(backrgound,(0,0))

        # 處理事件，當使用者關閉視窗時結束程式
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mX,mY=event.pos
                ball1['pos'][0]=mX
                ball1['pos'][1]=mY

        b1.update_ball(b2,ball1,screen_width, screen_height)
        b1.draw_ball(ball1)   
        b2.update_ball(b1,ball2,screen_width, screen_height)
        b2.draw_ball(ball2)        
        pygame.display.update()

    # add your code here  
   
    # 更新球的位置及反彈邏輯
    
        # add your code here
    
    # add your code here
    pygame.quit()

if __name__ == "__main__":
    main()