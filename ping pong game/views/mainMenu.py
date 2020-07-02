import arcade

from classes.bottun import Button


class MainMenu(arcade.View):
    def __init__(self, list_of_views, window_width, window_height):
        super().__init__()
        self.list_of_views = list_of_views
        self.window_width = window_width
        self.window_height = window_height
        self.title = "Ping Pong Game"
        self.font_size = 50
        self.text_title = arcade.draw_text(text=self.title,
                                           start_x=(self.window_width / 2 - ((len(self.title) * self.font_size) / 4)),
                                           start_y=self.window_height - 1.4 * self.font_size,
                                           color=arcade.color.BLACK,
                                           font_size=self.font_size
                                           )

        self.button_start = Button(400, 550 - 1.4 * self.font_size, 100, 50, "Start", arcade.color.GREEN,
                                   arcade.color.DARK_GREEN,
                                   arcade.color.WHITE, 30)
        self.button_exit = Button(400, 490 - 1.4 * self.font_size, 100, 50, "Exit", arcade.color.RED,
                                  arcade.color.DARK_RED,
                                  arcade.color.WHITE, 30)
        self.temp = arcade.Sprite("paddle_green.png", 1, center_y=200, center_x=200)

    def setup(self):
        """ This should set up your game and get it ready to play """

    def on_show(self):
        self.button_start.is_click = False
        self.button_start.is_hover = False
        self.button_exit.is_click = False
        self.button_exit.is_hover = False
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw everything for the game. """
        arcade.start_render()
        self.temp.draw()
        self.text_title.draw()
        self.button_start.draw()
        self.button_exit.draw()

    def on_key_press(self, key, _modifiers):
        """ Handle keypresses. In this case, we'll just count a 'space' as
        game over and advance to the game over view. """
        if key == arcade.key.ESCAPE:
            self.window.close()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.button_exit.on_mouse_press(x, y)
        self.button_start.on_mouse_press(x, y)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.button_exit.on_mouse_motion(x, y)
        self.button_start.on_mouse_motion(x, y)

    def on_update(self, delta_time: float):
        if self.button_exit.is_click:
            self.window.close()
        if self.button_start.is_click:
            self.window.show_view(self.list_of_views['games menu'])

