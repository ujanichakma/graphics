import numpy as np
import turtle

# A triangle
shape = np.array([
    [1, 1],
    [4, 1],
    [2.5, 4],
    [1, 1]
], dtype=float)

# Translation values
tx, ty = 3, 2

translated = shape.copy()
translated[:, 0] += tx
translated[:, 1] += ty

print("Original points:\n", shape)
print("Translated points:\n", translated)

#Turtle visualization
screen = turtle.Screen()
screen.setup(1000, 800)
screen.title("2D Translation")

t = turtle.Turtle()
t.speed(0)

max_value = max(
    np.max(np.abs(shape)),
    np.max(np.abs(translated))
)

scale = 250 / max_value

#Draw X axis
t.pencolor("gray")
t.penup()
t.goto(-400, 0)
t.pendown()
t.goto(400, 0)
t.write("X", font= ("Arial", 14))

#Draw Y axis
t.penup()
t.goto(0, -300)
t.pendown()
t.goto(0, 300)
t.write("Y", font = ("Arial",14))

#Original Triangle
t.pencolor("blue")

x, y = shape[0]
t.penup()
t.goto(x*scale, y*scale)
t.pendown()
t.write("Original", font = ("Arial",14))

for x,y in shape[1:]:
    t.goto(x*scale, y*scale)

#Translated Triangle
t.pencolor("red")

x,y = translated[0]
t.penup()
t.goto(x*scale, y*scale)
t.pendown()

for x,y in translated[1:]:
    t.goto(x*scale, y*scale)

t.hideturtle()
turtle.done()
