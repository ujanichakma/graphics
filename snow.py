import turtle
import math

def koch_curve(p1, p2, depth):
    if depth <= 0:
        return [p1, p2]

    x1, y1 = p1
    x2, y2 = p2

    a = (
        x1 + (x2 - x1) / 3,
        y1 + (y2 - y1) / 3
    )    
    b = (
        x1 + 2*(x2 - x1) / 3,
        y1 + 2*(y2 - y1) / 3
    )

    angle = math.radians(-60)

    vx = b[0] - a[0]
    vy = b[1] - a[1]

    peak = (
        a[0] + vx*math.cos(angle) - vy*math.sin(angle),
        a[1] + vx*math.sin(angle) + vy*math.cos(angle)
    )

    part1 = koch_curve(p1, a, depth-1)
    part2 = koch_curve(a, peak, depth-1)
    part3 = koch_curve(peak, b, depth-1)
    part4 = koch_curve(b, p2, depth-1)

    return part1[:-1]+part2[:-1]+part3[:-1]+part4

#equilateral triangle
p1 = (0, 150)
p2 = (-130, -75)
p3 = (130, -75)

depth = 4

side1 = koch_curve(p1, p2, depth)
side2 = koch_curve(p2, p3, depth)
side3 = koch_curve(p3, p1, depth)

points = side1[:-1]+side2[:-1]+side3

#turtle visualization
screen = turtle.Screen()
screen.setup(1000, 800)
screen.title("Koch snowflake")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.color("purple")

#start drawing
x, y = points[0]

t.penup()
t.goto(x, y)
t.pendown()

for x,y in points[1:]:
    t.goto(x, y)

#close snowflake
t.goto(points[0])

turtle.done()
