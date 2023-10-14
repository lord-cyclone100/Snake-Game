from turtle import Turtle

POSITIONS = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        # n = 0
        for i in POSITIONS:
            self.add_segment(i)

    def add_segment(self,i):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.goto(i)
        self.turtles.append(t)

    # def extend(self):
    #     self.add_segment(self.turtles[-1].i())
    def extend(self):
        last_position = self.turtles[-1].position()
        self.add_segment(last_position)

    def move_snake(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[i - 1].xcor()
            new_y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(x=new_x, y=new_y)
        self.turtles[0].forward(20)

    def move_up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def move_down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    def move_right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)

    def move_left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)