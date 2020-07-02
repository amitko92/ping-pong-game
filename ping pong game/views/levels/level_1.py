import arcade
import init

from classes.ball import Ball
from classes.paddle import Paddle


class Level_1(arcade.View):
    def __init__(self, width, height, paddle_size, paddle_color, go_back_view):
        super().__init__()

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



    def bonus_score_display(self):
        if self.counter_ball_is_speeding > 1:
            arcade.draw_text(str(self.counter_ball_is_speeding), self.width / 2, self.height / 2,
                             arcade.color.RED, 50)

    def on_draw(self):

        arcade.start_render()

        self.score_display()
        self.speed_display()
        self.bonus_score_display()

        self.left_player.draw()
        self.right_player.draw()

        self.ball.draw()
        self.window.flip()

        arcade.finish_render()

    def on_update(self, delta_time: float):
        if not self.is_collide_borders(self.left_player):
            self.left_player.on_update()

        if not self.is_collide_borders(self.right_player):
            self.right_player.on_update()

        self.is_ball_collide()
        self.ball.on_update()

        if self.player_2_score > 15 or self.player_1_score > 15:
            self.window.show_view(self.go_back_view)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.window.show_view(self.go_back_view)

        self.left_player.on_key_press(symbol)
        self.right_player.on_key_press(symbol)

    def on_key_release(self, key, modifiers):
        self.left_player.on_key_release(key)
        self.right_player.on_key_release(key)

    def is_collide_borders(self, player):
        if 0 >= player.bottom:
            player.center_y = 1 + (player.height / 2)
            return True
        if player.top >= self.height:
            player.center_y = self.height - ((player.height / 2) + 0.5)
            return True

    def is_ball_collide(self):

        # player 2 won
        if self.ball.center_x + (self.ball.width / 2) >= self.width:
            self.player_2_score += self.counter_ball_is_speeding
            self.counter_ball_is_speeding = 1
            self.ball.reset()

        # player 1 won
        if self.ball.center_x - (self.ball.width / 2) <= 0:
            self.player_1_score += self.counter_ball_is_speeding
            self.counter_ball_is_speeding = 1
            self.ball.reset()

        # ball bounce the wall
        if self.ball.center_y + (self.ball.height / 2) >= self.height:
            self.ball.direction_movement_y *= -1

        # ball bounce the wall
        if self.ball.center_y - (self.ball.height / 2) <= 0:
            self.ball.direction_movement_y *= -1

        # ball collide the paddle
        if self.ball.collides_with_sprite(self.left_player):
            self.ball_collide_with_paddle(self.left_player)

            if self.ball.is_speeding:
                self.counter_ball_is_speeding += 1
            else:
                self.counter_ball_is_speeding = 1

        # ball collide the paddle
        if self.ball.collides_with_sprite(self.right_player):
            self.ball_collide_with_paddle(self.right_player)
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

    def on_show(self):
        """ Called when switching to this view"""
        self.setup()
        arcade.set_background_color(arcade.color.BLACK)
        self.window.set_update_rate(1 / 50)

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

