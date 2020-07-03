import arcade


class Entity(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y, width, height, speed_x=1,
                 speed_y=1, direction_movement_x=1, direction_movement_y=1):
        super().__init__(filename=image, scale=scale)
        self.center_x = center_x
        self.center_y = center_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.direction_movement_x = direction_movement_x
        self.direction_movement_y = direction_movement_y
