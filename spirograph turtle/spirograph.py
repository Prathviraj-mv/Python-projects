from turtle import Turtle, Screen

s = Screen()
s.title("heart shape")
s.bgcolor("black")
t = Turtle()
t.color("red")
t.pensize(1)
t.speed(1000)
t.shape("circle")


def draw():
    n = 0
    while n < 60:
        t.hideturtle()
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.left(120)
        t.circle(100, 200)
        t.forward(250)
        t.right(265)
        t.forward(250)
        t.circle(100, 210)
        t.forward(200)
        t.circle(100, 400)

        n = n + 1


draw()
s.exitonclick()
