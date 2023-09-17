from turtle import Turtle

POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_block = []
        for i in range(3):
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(POS[i])
            self.snake_block.append(snake)


    def move(self):
        for snakes in range(len(self.snake_block) - 1, 0, -1):
            new_x = self.snake_block[snakes - 1].xcor()
            new_y = self.snake_block[snakes - 1].ycor()
            self.snake_block[snakes].goto(new_x, new_y)
        self.snake_block[0].forward(MOVE)

    def up(self):
        if self.snake_block[0].heading() != DOWN:
            self.snake_block[0].setheading(90)

    def down(self):
        if self.snake_block[0].heading() != UP:
            self.snake_block[0].setheading(270)

    def right(self):
        if self.snake_block[0].heading() != LEFT:
            self.snake_block[0].setheading(0)

    def left(self):
        if self.snake_block[0].heading() != RIGHT:
            self.snake_block[0].setheading(180)


    def new_square(self):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        self.snake_block.append(snake)
