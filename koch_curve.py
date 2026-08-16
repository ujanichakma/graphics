import turtle
import math

def koch_curve(p1, p2, depth):
    if depth == 0:
        return [p1, p2]

    x1, y1 = p1
    x2, y2 = p2

    a = (
        x1 + (x2-x1)/3,
        y1 + (y2-y1)/3
    )    
    b = (
        x1 + 2*(x2-x1)/3,
        y1 + 2*(y2-y1)/3
    )

    angle = math.radians(60)

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

    return part1[:-1] + part2[:-1] + part3[:-1] + part4

#input
start = (-4, -2)
end = (6, 5)
depth = 4

points = koch_curve(start, end, depth)

#Turtle visualize
screen = turtle.Screen()
screen.setup(1000, 800)
screen.title("Koch Curve")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

x_values = [p[0] for p in points]
y_values = [p[1] for p in points]

min_x = min(x_values)
max_x = max(x_values)
min_y = min(y_values)
max_y = max(y_values)

width = abs(max_x - min_x)
height = abs(max_y - min_y)

scale_x = 800 / width
scale_y = 500 / height
scale = min(scale_x, scale_y)

center_x = (min_x + max_x) / 2
center_y = (min_y + max_y) / 2

#start drawing
x, y = points[0]

t.penup()
t.goto(
    (x - center_x)*scale,
    (y - center_y)*scale
)
t.pendown()

for x,y in points[1:]:
    t.goto(
    (x - center_x)*scale,
    (y - center_y)*scale
)

turtle.done()
