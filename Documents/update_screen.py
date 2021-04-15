from settings import Settings
import pygame
from ship import Ship
def up_screen(ai_setting,screen,alien_ship):
    # 让绘制屏幕可见
    screen.fill(ai_setting.bg_color)
    alien_ship.blitme()
    pygame.display.flip()