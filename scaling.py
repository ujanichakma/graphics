import numpy as np 
import turtle

shape = np.array([
    [1, 1],
    [4, 1],
    [2.5, 4],
    [1, 1]
], dtype = float)

sx = 1.5
sy = 2.0

scaled = shape.copy()
scaled[:,0] *= sx
scaled[:,1] *= sy

print("Original points : \n", shape)
print("Scaled points : \n", scaled)

#Turtle visualization
screen = turtle.Screen()
screen.setup(1000, 800)
screen.title("2D scaling about origin ")

t = turtle.Turtle()
t.speed(0)

max_value = max(
    np.max(np.abs(shape)),
    np.max(np.abs(scaled))
)

scale = 250 / max_value

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

#Draw Original Triangle
t.pencolor("blue")

x,y = shape[0]
t.penup()
t.goto(x*scale, y*scale)
t.pendown()

for x, y in shape[1:]:
    t.goto(x*scale, y*scale)

#Draw Scaled shape
t.pencolor("red")

x,y = scaled[0]
t.penup()
t.goto(x*scale, y*scale)
t.pendown()

for x,y in scaled[1:]:
    t.goto(x*scale, y*scale)

t.hideturtle()
turtle.done()
