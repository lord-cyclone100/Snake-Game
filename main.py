from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

s = Screen()
s.bgcolor("black")
s.setup(width=700,height=700)
s.delay(10)
s.tracer(0)

snake = Snake()
food = Food()
score = Score()

s.listen()
s.onkey(fun=snake.move_up,key="Up")
s.onkey(fun=snake.move_down,key="Down")
s.onkey(fun=snake.move_left,key="Left")
s.onkey(fun=snake.move_right,key="Right")


switch_on = True
while switch_on:
    s.update()
    time.sleep(0.15)
    snake.move_snake()

    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.inc_score()


    if snake.turtles[0].xcor() > 330 or snake.turtles[0].xcor() < -330 or snake.turtles[0].ycor() > 330 or snake.turtles[0].ycor() < -330:
        switch_on = False
        score.game_over()

    for i in snake.turtles[1:]:
        if snake.turtles[0].distance(i) < 10:
            switch_on = False
            score.game_over()


s.exitonclick()