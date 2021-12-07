from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.7)
        self.color("blue")
        self.speed("fastest")
        self.rand_xy_pos = random.randint(-280, 280)
        self.place_food(self.rand_xy_pos, self.rand_xy_pos)

    def place_food(self, x_pos, y_pos):
        self.goto(x_pos, y_pos)

    def refresh(self):
        self.rand_new_xy_pos = random.randint(-280, 280)
        self.place_food(self.rand_new_xy_pos, self.rand_new_xy_pos)