from turtle import Turtle
import pong_constants
class User:
    name = ""
    score = 0
    userGraphic = None
    def __init__(self, name, player_number):
        self.name = name
        self.score = 0
        self.userGraphic = Turtle(pong_constants.PLAYER_SHAPE)
        self.userGraphic.shapesize(pong_constants.PLAYER_SHAPE_Y, pong_constants.PLAYER_SHAPE_X)
        self.userGraphic.color(pong_constants.PLAYER_COLOR)
        self.userGraphic.penup()

        # Setting up score graphic
        self.scoreGraphic = Turtle()
        self.scoreGraphic.penup()
        self.scoreGraphic.hideturtle()
        if player_number:
            self.scoreGraphic.goto(50, 400)
        else:
            self.scoreGraphic.goto(-50, 400)
        self.writeScoreOnView()

    def writeScoreOnView(self):
        self.scoreGraphic.clear()
        self.scoreGraphic.write(f"{self.score}", align="center", font=("Arial", 25, "normal"))

    def incrementScore(self):
        self.score += 1
        self.writeScoreOnView()
        
    def returnScore(self):
        return self.score
    
    def returnName(self):
        return self.name

    def moveTo(self, x_coord, y_coord):
        self.userGraphic.goto(x_coord, y_coord)

    def moveUp(self, height):
        x_coord = self.userGraphic.xcor()
        y_coord = self.userGraphic.ycor() + 25
        if y_coord <= height:
            self.userGraphic.goto(x_coord, y_coord)
        else:
            self.userGraphic.goto(x_coord, height)

    def moveDown(self, height):
        x_coord = self.userGraphic.xcor()
        y_coord = self.userGraphic.ycor() - 25
        if y_coord >= height:
            self.userGraphic.goto(x_coord, y_coord)
        else:
            self.userGraphic.goto(x_coord, height)

    def getCoords(self):
        return self.userGraphic.xcor(), self.userGraphic.ycor()
