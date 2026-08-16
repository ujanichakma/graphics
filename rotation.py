import matplotlib.pyplot as plt
import numpy as np
import math
import turtle

shape = np.array([
    [1, 1],
    [4, 1],
    [2.5, 4],
    [1, 1]
], dtype=float)

angle_deg = 45
theta = math.radians(angle_deg)

rotation_matrix = np.array([
    [math.cos(theta), -math.sin(theta)],
    [math.sin(theta),  math.cos(theta)]
])

rotated = shape @ rotation_matrix.T

print("Original points:\n", shape)
print("Rotated points:\n", rotated)

'''
plt.plot(shape[:, 0], shape[:, 1], marker="o", label="Original")
plt.plot(rotated[:, 0], rotated[:, 1], marker="o", label=f"Rotated {angle_deg}°")

plt.title("2D Rotation About Origin")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()
'''
#Turtle
screen = turtle.Screen()
screen.setup(1000,800)
screen.title("2D Rotation about origin")

t = turtle.Turtle()
t.speed(0)

max_value = max(
    np.max(np.abs(shape)),
    np.max(np.abs(rotated))
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

#Draw original shape
t.pencolor("blue")

x,y = shape[0]

t.penup()
t.goto(x*scale, y*scale)
t.pendown()

for x,y in shape[1:]:
    t.goto(x*scale, y*scale)

#Draw Rotated shape
t.pencolor("red")
x,y = rotated[0]

t.penup()
t.goto(x*scale, y*scale)
t.pendown()

for x,y in rotated[1:]:
    t.goto(x*scale, y*scale)

t.hideturtle()
turtle.done()
