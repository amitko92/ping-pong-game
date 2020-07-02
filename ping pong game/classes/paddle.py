import arcade
import init
from classes import entity
import time
import math


class Paddle(entity.Entity):
    def __init__(self, image, center_x, direction_movement_x, key_up, key_down, key_speed, key_push):

        super().__init__(image, init.paddle_scale, center_x, init.paddle_center_y, init.paddle_image_width,
                         init.paddle_image_height, init.paddle_speed, init.paddle_speed, direction_movement_x,
                         init.paddle_direction_movement_y)

        self.home_x = center_x
        self.max_speed = init.paddle_speed_max
        self.current_speed_power = init.paddle_max_speed_power
        self.max_speed_power = init.paddle_max_speed_power
        self.is_moving = False
        self.is_speeding = False
        self.is_pushing = False
        self.is_returning = False
        self.speed_press_last_time = time.time()
        self.key_speed = key_speed
        self.key_up = key_up
        self.key_down = key_down
        self.key_push = key_push

    def on_update(self, delta_time: float = 1 / 30):

        if self.is_speeding:
            self.key_speed_pressing()
        else:
            self.key_speed_release()

        if self.is_pushing:
            if math.sqrt((self.center_x - self.home_x) ** 2) < self.height * 3:
                self.center_x += self.max_speed * self.direction_movement_x
            else:
                self.is_pushing = False
                self.is_returning = True
                self.direction_movement_x *= -1  # to change the direction to returning
        elif self.is_returning:
            if self.center_x > self.home_x:
                self.center_x += self.max_speed * self.direction_movement_x
            else:
                self.is_returning = False
                self.direction_movement_x *= -1  # to change the direction to pushing
                self.center_x = self.home_x
        elif self.is_moving:
            if self.is_speeding and self.current_speed_power > 0:
                self.center_y += self.max_speed * self.direction_movement_y

            self.center_y += self.speed_y * self.direction_movement_y

    def key_speed_pressing(self):
        if time.time() - self.speed_press_last_time > 0.5:
            self.speed_press_last_time = time.time()
            if self.current_speed_power > 0:
                self.current_speed_power -= 1

    def key_speed_release(self):
        if time.time() - self.speed_press_last_time > 1:
            self.speed_press_last_time = time.time()
            if self.current_speed_power < self.max_speed_power:
                self.current_speed_power += 1

    def on_key_press(self, symbol: int):

        if symbol == self.key_up:
            self.direction_movement_y = 1
            self.is_moving = True
        elif symbol == self.key_down:
            self.direction_movement_y = -1
            self.is_moving = True

        if symbol == self.key_push:
            self.is_pushing = True

        if symbol == self.key_speed:
            self.is_speeding = True

    def on_key_release(self, key):
        if key == self.key_up or key == self.key_down:
            self.is_moving = False

        if key == self.key_speed:
            self.is_speeding = False
