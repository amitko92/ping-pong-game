import arcade

from classes.bottun import Button


class GameMenu(arcade.View):
    def __init__(self, list_of_views, window_width, window_height, go_back_view):
        super().__init__()
        self.go_back_view = go_back_view
        self.list_of_views = list_of_views
        self.window_width = window_width
        self.window_height = window_height
        self.title = "Game Menu"
        self.font_size = 50
        self.button_font_size = 30
        self.text_title = arcade.draw_text(text=self.title,
                                           start_x=(self.window_width / 2 - ((len(self.title)*self.font_size) / 4)),
                                           start_y=self.window_height - 1.4 * self.font_size,
                                           color=arcade.color.BLACK,
                                           font_size=self.font_size
                                           )

        self.button_player_vs_player = Button(400, 550 - 1.4 * self.button_font_size, 240, 50, "player vs player", arcade.color.GREEN, arcade.color.DARK_GREEN,
                                   arcade.color.WHITE, self.button_font_size)

        self.button_player_vs_wall = Button(400, 490 - 1.4 * self.button_font_size, 240, 50, "player vs wall", arcade.color.GREEN, arcade.color.DARK_GREEN,
                                   arcade.color.WHITE, self.button_font_size)

        self.button_meteor = Button(400, 430 - 1.4 * self.button_font_size, 240, 50, "meteor level", arcade.color.GREEN, arcade.color.DARK_GREEN,
                                   arcade.color.WHITE, self.button_font_size)

        self.button_exit = Button(400, 370 - 1.4 * self.button_font_size, 240, 50, "Exit", arcade.color.RED, arcade.color.DARK_RED,
                                  arcade.color.WHITE, self.button_font_size)

    def setup(self):
        self.button_player_vs_player.is_click = False
        self.button_player_vs_player.is_hover = False
        self.button_player_vs_wall.is_click = False
        self.button_player_vs_wall.is_hover = False
        self.button_meteor.is_click = False
        self.button_meteor.is_hover = False
        self.button_exit.is_click = False
        self.button_exit.is_hover = False

    def on_show(self):
        """ Called when switching to this view"""
        self.setup()
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw everything for the game. """
        arcade.start_render()
        self.text_title.draw()
        self.button_player_vs_wall.draw()
        self.button_player_vs_player.draw()
        self.button_meteor.draw()
        self.button_exit.draw()

    def on_key_press(self, key, _modifiers):
        """ Handle keypresses. In this case, we'll just count a 'space' as
        game over and advance to the game over view. """
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.go_back_view)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.button_exit.on_mouse_press(x, y)
        self.button_player_vs_wall.on_mouse_press(x, y)
        self.button_player_vs_player.on_mouse_press(x, y)
        self.button_meteor.on_mouse_press(x, y)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.button_exit.on_mouse_motion(x, y)
        self.button_player_vs_wall.on_mouse_motion(x, y)
        self.button_player_vs_player.on_mouse_motion(x, y)
        self.button_meteor.on_mouse_motion(x, y)

    def on_update(self, delta_time: float):
        if self.button_exit.is_click:
            self.window.show_view(self.go_back_view)
        if self.button_player_vs_player.is_click:
            self.window.show_view(self.list_of_views.get('level 1'))
        if self.button_player_vs_wall.is_click:
            self.window.show_view(self.list_of_views.get('level wall'))
        if self.button_meteor.is_click:
            self.window.show_view(self.list_of_views.get('level meteor'))

