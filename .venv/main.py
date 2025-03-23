from turtle import Turtle, Screen
import time
from game import Game
import pong_constants


screen = Screen()
screen.setup(width=pong_constants.SCREEN_WIDTH + 80, height=pong_constants.SCREEN_HEIGHT + 80)
screen.title("Pong game")
screen.bgcolor("white")
screen.tracer(0)

screen.update()
player_1_name = "Player ONE"
player_2_name = "Player TWO"
win_threshold = 5
game = Game(player_1_name, player_2_name, win_threshold, pong_constants.SCREEN_WIDTH, pong_constants.SCREEN_HEIGHT)
screen.update()

def player1DirectionUp():
    game.movePlayerUp(1)
def player1DirectionDown():
    game.movePlayerDown(1)
def player2DirectionUp():
    game.movePlayerUp(2)
def player2DirectionDown():
    game.movePlayerDown(2)

screen.listen()
screen.onkey(player1DirectionUp, "w")
screen.onkey(player1DirectionDown, "s")
screen.onkey(player2DirectionUp, "Up")
screen.onkey(player2DirectionDown, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    game_condition = game.moveBall()
    if game_condition == 1:
        game.pointWon(player_1_name)
        game.restartGame()
    elif game_condition == 2:
        game.pointWon(player_2_name)
        game.restartGame()

    win_check = game.checkIfWon(win_threshold)
    if win_check == 1:
        game.finalWinner(player_1_name + " Won")
        game_is_on = False
    elif win_check == 2:
        game.finalWinner(player_2_name + " Won")
        game_is_on = False
    screen.update()

screen.exitonclick()
    