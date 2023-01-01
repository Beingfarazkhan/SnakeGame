import turtle
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=700, height=700)

screen.bgcolor("black")
screen.title("My Snake Game ")
screen.tracer(0)
user_choice = screen.textinput("Select Game Mode ", "Choose difficulty level Type 'easy' for infinite wall and 'hard' for finite wall  " )

snake = Snake()

food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=snake.up , key="Up")
screen.onkey(fun=snake.down , key="Down" )
screen.onkey(fun=snake.left , key="Left" )
screen.onkey(fun=snake.right , key="Right" )

game_is_on = True

while game_is_on :
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15 :
        food.refresh()
        scoreboard.increase_score()

        snake.extend()
# detect collision with wall
    if user_choice.lower() == "hard":
        if snake.head.xcor() >= 350 or snake.head.ycor() >= 350 or snake.head.xcor() <= -340 or snake.head.ycor() <= -340:
            scoreboard.reset()
            snake.reset()
    else:
        snake.infinite_wall()

    # detection of collision with snake tail
    for segment in snake.segments[1:] :
        if segment == snake.head :
            pass
        if snake.head.distance(segment) < 10 :
            scoreboard.reset()
            snake.reset()



screen.exitonclick()