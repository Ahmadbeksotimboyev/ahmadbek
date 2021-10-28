# from turtle import Screen, Turtle 

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")

# starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.goto(position)


# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)

from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

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


screen.exitonclick()

