import arcade

from classes.bottun import Button


class CommendViews(arcade.View):
    def __init__(self, list_of_views, window_width, window_height):
        super().__init__()
        self.list_of_views = list_of_views
        self.window_width = window_width
        self.window_height = window_height
        self.play = None
        self.button_player_vs_wall = None
        self.button_exit = None

    def setup(self):
        self.play = Button(400, 550, 100, 50, "play", arcade.color.GREEN, arcade.color.DARK_GREEN,
                           arcade.color.DARK_GREEN, 30)

        self.button_exit = Button(400, 490, 100, 50, "Exit", arcade.color.RED, arcade.color.DARK_RED,
                                  arcade.color.DARK_RED, 30)

    def on_show(self):
        self.setup()
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)

    def on_update(self, delta_time: float):
        if self.play.is_click:
            self.window.show_view(self.list_of_views.get('level 1'))
        if self.button_exit.is_click:
            self.window.close()

    def on_draw(self):
        """ Draw everything for the game. """
        arcade.start_render()
        self.play.draw()
        self.button_exit.draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if self.button_exit.collides_with_point([x, y]):
            self.button_exit.is_click = True
        if self.play.collides_with_point([x, y]):
            self.play.is_click = True

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if self.button_exit.collides_with_point([x, y]):
            self.button_exit.is_hover = True
        if self.play.collides_with_point([x, y]):
            self.play.is_hover = True

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            self.window.close()
