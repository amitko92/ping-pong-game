import arcade
import init
from classes import entity


class Meteor(entity.Entity):
    def __init__(self, scale=1, center_x=400, center_y=250):
        super().__init__(init.meteor_image, scale, center_x, center_y, init.meteor_image_width,
                         init.meteor_image_height, init.meteor_speed_x, init.meteor_speed_y,
                         init.meteor_direction_movement_x, init.meteor_direction_movement_y)

    def on_update(self, delta_time: float = 1 / 60):
        self.movement(delta_time)

    def movement(self, delta_time):
        self.center_x += self.direction_movement_x * self.speed_x * delta_time
        self.center_y += self.direction_movement_y * self.speed_y * delta_time
