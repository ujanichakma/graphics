import turtle
import math

#sample endpoints
x1, y1 = 2, 3
x2, y2 = 12, 9

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps =  math.ceil(max(abs(dx), abs(dy)))
    if steps == 0:
        return [(round(x1), round(y1))]

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1
    points = []

    for _ in range(steps+1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc
    return points
points = dda(x1, y1, x2, y2)
print("Generated pixels : ",points)

#Turtle
screen = turtle.Screen()
screen.setup(1000, 800)
screen.title("DDA line")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

#scale
max_value = max(
    abs(x1), abs(y1),
    abs(x2), abs(y2),
    1
)
scale = 300 / max_value

#draw x axis
t.pencolor("gray")
t.penup()
t.goto(-400, 0)
t.pendown()
t.goto(400, 0)
t.write("X", font = ("Arial", 14))

#Draw Y axis
t.penup()
t.goto(0, -300)
t.pendown()
t.goto(0, 300)
t.write("Y", font = ("Arial", 14))

#Draw pixels
t.pencolor("red")
for x, y in points:
    t.penup()
    t.goto(x*scale, y*scale)
    t.dot(6)
#Draw line
t.pencolor("blue")
t.penup()
t.goto(x1*scale, y1*scale)
t.pendown()
t.goto(x2*scale, y2*scale)

#point A
t.penup()
t.goto(x1*scale, y1*scale)
t.pendown()
t.write("A", font = ("Arial", 14))

#point B
t.penup()
t.goto(x2*scale, y2*scale)
t.pendown()
t.write("B", font = ("Arial", 14))

turtle.done()
