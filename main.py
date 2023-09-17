from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)
scoreboard = Score()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
is_game = True
while is_game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_block[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.new_square()
    if snake.snake_block[0].xcor() > 280 or snake.snake_block[0].xcor() < -280 or snake.snake_block[0].ycor() < -280 or snake.snake_block[0].ycor() > 280:
        is_game = False
        scoreboard.game_over()
    for block in snake.snake_block:
        if block == snake.snake_block[0]:
            pass
        elif snake.snake_block[0].distance(block) < 10:
            is_game = False
            scoreboard.game_over()
screen.exitonclick()
