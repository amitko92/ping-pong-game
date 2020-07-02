import arcade


class Button(arcade.Sprite):
    def __init__(self, width, height, dw, dh, text, background_color, hover_background_color, text_color, font_size):
        super().__init__()
        self.center_x = width
        self.center_y = height
        self.background_color = background_color
        self.hover_background_color = hover_background_color
        self.width = dw
        self.height = dh
        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        self.is_click = False
        self.is_hover = False

    def draw(self):
        if self.is_hover:
            arcade.draw_rectangle_filled(center_x=self.center_x, center_y=self.center_y,
                                         color=self.hover_background_color, width=self.width, height=self.height)
        else:
            arcade.draw_rectangle_filled(center_x=self.center_x, center_y=self.center_y,
                                         color=self.background_color, width=self.width, height=self.height)

        arcade.draw_text(self.text, self.center_x - (self.font_size*len(self.text) / 4), self.center_y - self.font_size / 2, arcade.color.BLACK, self.font_size)

    def on_mouse_press(self, x: float, y: float):
        if self.collides_with_point([x, y]):
            self.is_click = True
        else:
            self.is_click = False

    def on_mouse_motion(self, x: float, y: float):
        if self.collides_with_point([x, y]):
            self.is_hover = True
        else:
            self.is_hover = False

