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

print("Generated pixels:", points)


# -----------------------
# Turtle Visualization
# -----------------------

screen = turtle.Screen()
screen.setup(1000,800)

t = turtle.Turtle()
t.speed(0)

max_value = max(
                abs(x1),
                abs(y1),
                abs(x2),
                abs(y2)
)

scale = 300/max_value


# X-axis draw
t.penup()
t.goto(-400, 0)
t.pendown()
t.goto(400, 0)
t.write("X", font = ("Arial", 14))


# Y-axis draw
t.penup()
t.goto(0, -300)
t.pendown()
t.goto(0, 300)
t.write("Y", font = ("Arial", 14))


# Bresenham line draw
t.color("green")

x, y = points[0]

t.penup()
t.goto(x * scale, y * scale)
t.write("A", font=("Arial", 12))
t.pendown()

'''for x, y in points[1:]:
    t.goto(x * scale, y * scale)  eta dile generated dot guloke line ta connect kore,tai akabaka line dekhabe
    t.dot(2)'''
t.goto(x2 * scale, y2 * scale) #eta dile straight line hobe,mane sudhu endpoint guloke connect korbe, generated point guloke connect krbe na line ta
t.write("B", font=("Arial", 12))

t.hideturtle()
turtle.done()
