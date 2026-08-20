import turtle

# sample endpoints
x1, y1 = 20, 10
x2, y2 = 30, 18

def bresenham(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    error = dx - dy
    while True:
        points.append((x1, y1))

        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * error

        if e2 > -dy:
            error = error - dy
            x1 = x1 + sx
        if e2 < dx:
            error = error + dx
            y1 = y1 + sy
    return points
points = bresenham(x1, y1, x2, y2)
print("Generated pixels : ", points)

#Turtle visualization
screen = turtle.Screen()
screen.setup(1000, 800)
screen.title("Bresenham Line")

t = turtle.Turtle()
t.speed()
t.hideturtle()

#scale
max_value = max(
    abs(x1), abs(y1),
    abs(x2), abs(y2),
    1
)
scale = 300 / max_value

#Draw X axis
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


#Draw generated pixels
t.pencolor("red")
for x,y in points:
    t.penup()
    t.goto(x*scale, y*scale)
    t.dot(6)
#Draw line
t.pencolor("blue")
t.penup()
t.goto(x1*scale, y1*scale)
t.pendown()
t.goto(x2*scale, y2*scale)

#starting point A
t.penup()
t.goto(x1*scale , y1*scale)
t.pendown()
t.write("A", font = ("Arial", 14))

#Ending point B
t.penup()
t.goto(x2*scale , y2*scale)
t.pendown()
t.write("B", font = ("Arial", 14))

turtle.done()
