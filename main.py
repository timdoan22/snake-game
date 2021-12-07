from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Squid Game")
screen.tracer(0)

score = Score()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 18:
        score.increase_score()
        snake.add_body()
        food.refresh()

    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    #Detect collision with its own body
    for snake_block in snake.snake_body[1:]:
        if snake.head.distance(snake_block) < 7:
            score.reset()
            snake.reset()
screen.exitonclick()
# first_block = snake_body[0]
# first_block.color("green")
