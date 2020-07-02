import arcade
from classes import entity
import init


class Block(entity.Entity):
    def __init__(self, center_x, center_y):
        super().__init__(init.box_image, init.box_scale, center_x, center_y, init.box_image_width, init.box_image_height)


