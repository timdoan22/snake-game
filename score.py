from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt") as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            with open("data.txt", "w") as data:
                self.high_score = self.score
                data.write(str(self.high_score))
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.show_score()

    def increase_score(self):
        self.score += 1
        self.show_score()
