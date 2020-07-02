import arcade
from PIL import Image
import init
from arcade import Sprite
from random import random
from classes import entity


class Ball(entity.Entity):
    def __init__(self):
        super().__init__(init.ball_image, init.ball_scale, init.ball_center_x, init.ball_center_y,
                         init.ball_image_width, init.meteor_image_height, init.ball_speed, init.ball_speed,
                         init.ball_direction_movement_x, init.ball_direction_movement_y)

        self.max_speed = init.max_ball_speed
        self.is_speeding = False

    def on_update(self, delta_time: float = 1 / 50):
        if self.is_speeding:
            self.center_x += self.direction_movement_x * self.max_speed
            self.center_y += self.direction_movement_y * self.max_speed
        else:
            self.center_x += self.direction_movement_x * self.speed_x
            self.center_y += self.direction_movement_y * self.speed_y

    def reset(self):
        self.center_x = init.ball_center_x
        self.center_y = init.ball_center_y
        self.is_speeding = False

        if random() > 0.5:
            self.direction_movement_x = -1
        if random() < 0.5:
            self.direction_movement_y = -1
