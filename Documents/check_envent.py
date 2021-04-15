import pygame
import sys
def check_envents():
    # 监听键盘和鼠标事件
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            sys.exit()