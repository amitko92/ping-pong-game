
# window:
window_width = 960
window_height = 640

# box
box_image = ":resources:images/tiles/boxCrate_double.png"
box_scale = 0.5
box_image_width = 64
box_image_height = 64

# paddle
paddle_center_y = window_height / 2
paddle_pixel_buffer = 1
paddle_scale = 1
paddle_speed = 5
paddle_speed_max = 7
paddle_max_speed_power = 5
paddle_image_width = 32
paddle_image_height = 96
paddle_direction_movement_y = 1

# right paddle:
paddle_right_image = "paddle_blue.png"
paddle_right_center_x = window_width - (paddle_image_width / 2) - box_image_width - paddle_pixel_buffer
paddle_right_direction_movement_x = -1
paddle_right_key_up = 65362
paddle_right_key_down = 65364
paddle_right_key_speed = 65363
paddle_right_key_push = 65361

# left paddle:
paddle_left_image = "paddle_green.png"
paddle_left_center_x = box_image_width + (paddle_image_width / 2) + paddle_pixel_buffer
paddle_left_direction_movement_x = 1
paddle_left_key_up = 119
paddle_left_key_down = 115
paddle_left_key_speed = 97
paddle_left_key_push = 100


# ball:
ball_image = ":resources:images/pinball/pool_cue_ball.png"
ball_scale = 0.5
ball_center_x = window_width / 2
ball_center_y = window_height / 2
ball_speed = 5
max_ball_speed = ball_speed*2 + 2
ball_direction_movement_x = 1
ball_direction_movement_y = 1
ball_image_width = 34
ball_image_height = 34

# meteor:
meteor_image = ":resources:images/space_shooter/meteorGrey_big3.png"
meteor_speed_x = 100
meteor_speed_y = 100
meteor_direction_movement_x = 1
meteor_direction_movement_y = 1
meteor_image_width = 64
meteor_image_height = 64
