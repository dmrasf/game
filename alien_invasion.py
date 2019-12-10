import sys
import  pygame
from pygame.sprite import Group

from settings import Setting
from ship import Ship
from game_stats import GameStats
from button import Button
import game_functions as gf

def run_game():
    # 初始化屏幕 创建一个屏幕对象
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")

    # 创建一艘   创建子弹  外星人
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()


    stats = GameStats(ai_settings)

    # 创建外星人s
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 游戏的循环
    while True:
        # 事件
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()