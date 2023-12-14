import turtle
import random

seed_value = random.random()
random.seed(seed_value)

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("white")
t.speed(0)
t.penup()
t.goto(0, 0)
t.pendown()

lines = 0
max_lines = 250

while True:
    if lines >= max_lines:
        lines = 0
        t.clear()

    angle = random.uniform(0, 360)
    distance = random.uniform(1, 100)
    color = (random.random(), random.random(), random.random())

    t.pencolor(color)

    x, y = t.position()

    if abs(x) > s.window_width() / 2:
        t.setx(x % (s.window_width() / 2) * (-1 if x > 0 else 1))

    if abs(y) > s.window_height() / 2:
        t.sety(y % (s.window_height() / 2) * (-1 if y > 0 else 1))

    t.setheading(angle)
    t.forward(distance)

    lines += 1
