import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.title("Snake")
screen.setup(height=800, width=800)
screen.bgcolor("black")
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segment[0].distance(food) < 15:
        scoreboard.increment()
        snake.extend()
        food.refresh()


    if snake.segment[0].xcor() >400 or snake.segment[0].xcor() <-400 or snake.segment[0].ycor() >400 or snake.segment[0].ycor() <-400 :
        scoreboard.gameover()
        game_is_on = False

    for x in snake.segment[1:]:

        if snake.segment[0].distance(x) <10:
            scoreboard.gameover()
            game_is_on = False
screen.exitonclick()