import  pygame
import sys
from settings import Settings
from ship import Ship
import check_envent as ck
import update_screen as up

def run_game():
    #初始化游戏，并创建一个屏幕对象
    ai_setting = Settings()
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    alien_ship = Ship(screen)
    pygame.display.set_caption("Alien Invasion")
    #开始游戏主循环
    while True:
        ck.check_envents()
        up.up_screen(ai_setting,screen,alien_ship)
run_game()
