from turtle import Turtle
from user import User
from ball import Ball

class Game:
    player_1 = None
    player_2 = None
    winThreshold = 0
    width = 0
    height = 0
    ball_graphic = None

    def __init__(self, name1, name2, winThreshold, screen_width, screen_height):
        self.player_1 = User(name1, 0)
        self.player_1.moveTo(-360, 0)
        self.player_2 = User(name2, 1)
        self.player_2.moveTo(360, 0)
        self.winThreshold = winThreshold
        self.width = screen_width/2
        self.height = screen_height/2

        self.generateBoundaries()

        self.ball_graphic = Ball(self.width, self.height)

    def moveBall(self):
        player_1_xcor, player_1_ycor = self.player_1.getCoords()
        player_2_xcor, player_2_ycor = self.player_2.getCoords()
        self.ball_graphic.detectCollisionOfBall(player_1_xcor, player_1_ycor, player_2_xcor, player_2_ycor)
        return self.ball_graphic.move()

    def restartGame(self):
        self.ball_graphic.resetGame()

    def generateBoundaries(self):
        # Setting up center line
        self.centerLine = Turtle()
        self.centerLine.hideturtle()
        self.centerLine.width(2)
        self.centerLine.color("red")
        self.centerLine.penup()
        self.centerLine.goto(0, self.height)
        self.centerLine.pendown()
        self.centerLine.goto(0, -self.height)
        self.centerLine.goto(-self.width, -self.height)
        self.centerLine.goto(-self.width, self.height)
        self.centerLine.goto(-self.width, self.height)
        self.centerLine.goto(self.width, self.height)
        self.centerLine.goto(self.width, -self.height)
        self.centerLine.goto(0, -self.height)

    def checkWinCondition(self):
        if self.player_1.returnScore() >= self.winThreshold:
            return 1
        elif self.player_2.returnScore() >= self.winThreshold:
            return 2
        return 0

    def pointWon(self, playerName):
        if self.player_1.returnName() == playerName:
            self.player_1.incrementScore()
        elif self.player_2.returnName() == playerName:
            self.player_2.incrementScore()

    def checkIfWon(self, win_threshold):
        if self.player_1.returnScore() == win_threshold:
            return 1
        elif self.player_2.returnScore() == win_threshold:
            return 2
        return 0

    def returnDisplayValues(self):
        return self.player_1.returnName(), self.player_1.returnName(), self.player_2.returnName(), self.player_2.returnName()
    
    def movePlayerUp(self, player):
        if player == 1:
            self.player_1.moveUp(self.height)
        else:
            self.player_2.moveUp(self.height)
            
    def movePlayerDown(self, player):
        if player == 1:
            self.player_1.moveDown(-self.height)
        else:
            self.player_2.moveDown(-self.height)

    def finalWinner(self, text):
        self.winner_text_graphic = Turtle()
        self.winner_text_graphic.penup()
        self.winner_text_graphic.hideturtle()
        self.winner_text_graphic.write(f"{text}", align="center", font=("Arial", 25, "normal"))