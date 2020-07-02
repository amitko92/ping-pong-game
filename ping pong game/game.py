import arcade
from views.levels import level_meteor
from views.GameMenu import GameMenu
from views.levels.level_1 import Level_1
from views.levels.level_wall import Level_wall
from views.mainMenu import MainMenu


class Game(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width=width, height=height, title="Different Views Minimal Example")
        self.set_update_rate(1 / 10)

        self.list = {}
        self.main_menu = MainMenu(self.list, width, height)

        self.level_1 = Level_1(self.width, self.height, [80, 20], arcade.color.WHITE, self.main_menu)
        self.level_wall = Level_wall(self.width, self.height, [80, 20], arcade.color.WHITE, self.main_menu)
        self.level_meteor = level_meteor.LevelMeteor(self.width, self.height, [80, 20], arcade.color.WHITE, self.main_menu)
        self.game_menu = GameMenu(self.list, width, height, self.main_menu)

        self.list['games menu'] = self.game_menu
        self.list['level wall'] = self.level_wall
        self.list['level 1'] = self.level_1
        self.list['level meteor'] = self.level_meteor

    def start(self):
        self.show_view(self.main_menu)
        arcade.run()
