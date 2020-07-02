import arcade
import init
from classes import meteor
from classes.ball import Ball
from classes.paddle import Paddle
from classes.block import Block


class LevelMeteor(arcade.View):
    def __init__(self, width, height, paddle_size, paddle_color, go_back_view, block_size=64):
        super().__init__()
        self.block_size = block_size
        self.up_and_down = arcade.SpriteList()
        self.right_wall = arcade.SpriteList()
        self.left_wall = arcade.SpriteList()
        offset_w = block_size / 2
        offset_h = block_size / 2

        # up and down walls
        for i in range(0, width, block_size):
            self.up_and_down.append(Block(offset_w + i, height - offset_w))
            self.up_and_down.append(Block(offset_w + i, offset_w))

        # right wall
        for i in range(0, height, block_size):
            self.right_wall.append(Block(width - offset_h, i + offset_h))

        # left wall
        for i in range(0, height, block_size):
            self.left_wall.append(Block(offset_w, i + offset_h))

        self.width = width
        self.height = height
        self.go_back_view = go_back_view

        self.paddle_size = paddle_size
        self.paddle_color = paddle_color

        self.player_1_score = 0
        self.player_2_score = 0
        self.counter_ball_is_speeding = 1

        self.ball_speed = 3
        self.max_ball_speed = 6

        # text box
        self.score_text_box_w = 350
        self.score_text_box_h = 70
        self.score_text_box_x = (self.width / 2)
        self.score_text_box_y = self.height - 20

        self.left_player = Paddle(init.paddle_left_image, init.paddle_left_center_x,
                                  init.paddle_left_direction_movement_x, init.paddle_left_key_up,
                                  init.paddle_left_key_down, init.paddle_left_key_speed, init.paddle_left_key_push)

        self.right_player = Paddle(init.paddle_right_image, init.paddle_right_center_x,
                                   init.paddle_right_direction_movement_x, init.paddle_right_key_up,
                                   init.paddle_right_key_down, init.paddle_right_key_speed, init.paddle_right_key_push)

        self.paddles = arcade.SpriteList()
        self.paddles.append(self.left_player)
        self.paddles.append(self.right_player)

        self.ball = Ball()

        self.meteor_1 = meteor.Meteor(center_x=width / 2, center_y=height / 2 + 128)
        self.meteor_2 = meteor.Meteor(center_x=width / 2, center_y=height / 2 - 128)
        self.meteors = arcade.SpriteList()
        self.meteors.append(self.meteor_1)
        self.meteors.append(self.meteor_2)

        self.paddles = arcade.SpriteList()
        self.paddles.append(self.left_player)
        self.paddles.append(self.right_player)

    def bonus_score_display(self):
        if self.counter_ball_is_speeding > 1:
            arcade.draw_text(str(self.counter_ball_is_speeding), self.width / 2, self.height / 2,
                             arcade.color.RED, 50)

    def on_draw(self):

        arcade.start_render()

        self.right_wall.draw()
        self.left_wall.draw()
        self.up_and_down.draw()

        self.score_display()
        self.speed_display()
        self.bonus_score_display()

        self.left_player.draw()
        self.right_player.draw()

        self.meteors.draw()

        self.ball.draw()
        self.window.flip()

        arcade.finish_render()

    def on_update(self, delta_time: float):

        self.players_collide_borders()
        self.left_player.on_update()
        self.right_player.on_update()

        self.is_meteors_collide_borders()
        self.meteors.on_update()

        self.is_ball_collide()
        self.ball.on_update()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.window.show_view(self.go_back_view)

        self.left_player.on_key_press(symbol)
        self.right_player.on_key_press(symbol)

    def on_key_release(self, key, modifiers):
        self.left_player.on_key_release(key)
        self.right_player.on_key_release(key)

    def players_collide_borders(self):
        temp = arcade.check_for_collision_with_list(self.left_player, self.up_and_down)
        if len(temp) > 0:
            self.left_player.direction_movement_y *= -1

        temp = arcade.check_for_collision_with_list(self.right_player, self.up_and_down)
        if len(temp) > 0:
            self.right_player.direction_movement_y *= -1

    def is_meteors_collide_borders(self):

        for m in self.meteors:
            temp = m.collides_with_list(self.up_and_down)
            if len(temp) > 0:
                print("collide")
                m.direction_movement_y *= -1

        for m in self.meteors:
            temp = m.collides_with_list(self.left_wall)
            temp += m.collides_with_list(self.right_wall)
            if len(temp) > 0:
                m.direction_movement_x *= -1

    def is_ball_collide(self):

        # meteors
        temp = self.ball.collides_with_list(self.meteors)
        if len(temp) > 0:
            self.ball.direction_movement_y *= -1
            self.ball.direction_movement_x *= -1

        # player 2 won
        temp = self.ball.collides_with_list(self.right_wall)
        if len(temp) > 0:
            self.player_2_score += self.counter_ball_is_speeding
            self.counter_ball_is_speeding = 1
            self.ball.reset()

        # player 1 won
        temp = self.ball.collides_with_list(self.left_wall)
        if len(temp) > 0:
            self.player_1_score += self.counter_ball_is_speeding
            self.counter_ball_is_speeding = 1
            self.ball.reset()

        # ball bounce the wall
        temp = self.ball.collides_with_list(self.up_and_down)
        if len(temp) > 0:
            self.ball.direction_movement_y *= -1

        # ball collide the paddle
        temp = self.ball.collides_with_list(self.paddles)
        if len(temp) > 0:
            self.ball_collide_with_paddle(temp[0])
            if self.ball.is_speeding:
                self.counter_ball_is_speeding += 1
            else:
                self.counter_ball_is_speeding = 1

    def ball_collide_with_paddle(self, paddle):
        self.ball.direction_movement_x *= -1

        if paddle.is_pushing:
            self.ball.direction_movement_y = 0
            self.ball.is_speeding = True

            paddle.is_returning = True
            paddle.is_pushing = False
            paddle.direction_movement_x *= -1
        elif not paddle.is_moving and self.ball.direction_movement_y == 0:
            self.ball.center_x += self.ball.max_speed * self.ball.direction_movement_x
            self.ball.direction_movement_y = 0
            self.ball.is_speeding = False
        elif paddle.is_moving:
            self.ball.direction_movement_y = paddle.direction_movement_y
            self.ball.is_speeding = False
            if paddle.is_speeding:
                self.ball.is_speeding = True
            else:
                self.ball.center_x += self.ball.max_speed * self.ball.direction_movement_x

    def setup(self):
        self.player_1_score = 0
        self.player_2_score = 0
        self.counter_ball_is_speeding = 1
        self.meteor_1 = meteor.Meteor(center_x=self.width / 2, center_y=self.height / 2 + 128)
        self.meteor_2 = meteor.Meteor(center_x=self.width / 2, center_y=self.height / 2 - 128)

    def on_show(self):
        """ Called when switching to this view"""
        self.setup()
        arcade.set_background_color(arcade.color.BLACK)
        self.window.set_update_rate(1 / 50)
        self.left_player.center_y = self.height / 2
        self.right_player.center_y = self.height / 2

    def score_display(self):

        arcade.draw_rectangle_outline(self.width / 2, self.height - 50, self.score_text_box_w, self.score_text_box_h,
                                      arcade.color.WHITE)

        # title of score box self.score_text_box_x + 20
        arcade.draw_text("score box", (self.width / 2) - 15, self.height - 35, arcade.color.WHITE, 12)
        # score player 1
        arcade.draw_text("Player 1 score: " + str(self.player_1_score), (self.width / 2 - 40) + 100, self.height - 80,
                         arcade.color.WHITE, 12)
        # score player 2
        arcade.draw_text("Player 2 score: " + str(self.player_2_score), (self.width / 2 - 60) - 100, self.height - 80,
                         arcade.color.WHITE, 12)

    def speed_display(self):
        # speed player 1
        arcade.draw_text(str(self.left_player.current_speed_power) + "/" + str(self.left_player.max_speed_power),
                         self.width - 30, 10, arcade.color.WHITE, 12)

        # speed player 2
        arcade.draw_text(str(self.right_player.current_speed_power) + "/" + str(self.right_player.max_speed_power), 10, 10,
                         arcade.color.WHITE, 12)
