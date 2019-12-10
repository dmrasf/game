class Setting:
    '''设置类'''

    def __init__(self):
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (230, 230, 230)

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 飞船设置
        self.ship_speed_factor = 0.8
        self.ship_limit = 3

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
