import random

from turtle import Turtle
import pong_constants


class Ball:
    def __init__(self, screen_width, screen_height):
        self.ball_graphic = Turtle(pong_constants.BALL_SHAPE)
        self.ball_graphic.color(pong_constants.BALL_COLOR)
        self.ball_graphic.penup()

        self.x_move = -5
        self.y_move = 10
        self.screen_width = screen_width
        self.screen_height = screen_height

    def resetGame(self):
        self.ball_graphic.goto(0, random.randrange(0, 100, 10))
        self.bounce_x()

    def move(self):
        x_coord = self.ball_graphic.xcor() + self.x_move
        y_coord = self.ball_graphic.ycor() + self.y_move
        self.ball_graphic.goto(x_coord, y_coord)
        if self.ball_graphic.ycor() >= self.screen_height or self.ball_graphic.ycor() <= -self.screen_height:
            self.bounce_y()
        elif self.ball_graphic.xcor() >= self.screen_width:
            # Player 2 lost
            return 1
        elif self.ball_graphic.xcor() <= -self.screen_width:
            # Player 1 lost
            return 2
        return 0

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def detectCollisionOfBall(self, player_1_xcor, player_1_ycor, player_2_xcor, player_2_ycor):
        if self.ball_graphic.distance((player_2_xcor, player_2_ycor)) < 50 and self.ball_graphic.xcor() > 340:
            self.bounce_x()
        elif self.ball_graphic.distance((player_1_xcor, player_1_ycor)) < 50 and self.ball_graphic.xcor() < -340:
            self.bounce_x()
