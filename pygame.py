import pygame, sys
from pygame.locals import *

# main
pygame.init()
# 設定視窗大小，可以改變參數設定成喜歡的大小。
DISPLAY = pygame.display.set_mode((800,600))

# 設定標題
pygame.display.set_caption("HELLO")
# 這邊會顯示黑色，可以透過修改參數的方式改成自己喜歡的顏色。
DISPLAY.fill((0,0,0)) 
# 無窮迴圈
while True:
    # 取得所有的Event
    for event in pygame.event.get():
        # 如果event是QUIT，也就是按右上角的x
        if event.type == pygame.QUIT:
            # 將pygame殺掉
            pygame.quit()
            # 終止程式
            sys.exit()
    # 一直更新pygame的畫面
    pygame.display.update()

