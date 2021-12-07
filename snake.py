from turtle import Turtle

MOVE_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[-1]

    def create_new_body(self, position):
        new_body = Turtle("square")
        new_body.penup()
        new_body.color("white")
        new_body.goto(self.x_pos, self.y_pos)
        self.snake_body.append(new_body)
        self.x_pos -= 20

    def reset(self):
        for body in self.snake_body:
            body.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for snake_block in range(3):
            self.create_new_body(snake_block)

    def add_body(self):
        self.create_new_body(self.tail.position())

    def move(self):
        for snake_part in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake_part - 1].xcor()
            new_y = self.snake_body[snake_part - 1].ycor()
            self.snake_body[snake_part].goto(new_x, new_y)
        self.head.forward(MOVE_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
