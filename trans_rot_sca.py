import numpy as np 
import math 
import turtle 

#original triangle
shape = np.array([
    [1, 1],
    [4, 1],
    [2.5, 4],
    [1, 1]
], dtype=float)

#center points 
cx = 2
cy = 2
center = np.array([cx, cy])

#Translation
tx = 3
ty = 2

translated = shape.copy()

translated[:, 0] += tx
translated[:, 1] += ty

#Rotation
angle_deg = 45
theta = math.radians(angle_deg)
rotation_matrix = np.array([
    [math.cos(theta), -math.sin(theta)],
    [math.sin(theta), math.cos(theta)]
])
rotated = (translated - center) @ rotation_matrix.T + center

#Scaling
sx = 1.5
sy = 2.0 

scaled = rotated.copy()
scaled[:, 0] = cx + (scaled[:, 0] - cx) * sx
scaled[:, 1] = cy + (scaled[:, 1] - cy) * sy

#print
print("Original points : \n", shape)
print("Translated points : \n", translated)
print("Rotated points : \n", rotated)
print("Scaled points : \n", scaled)

#Turtle
screen = turtle.Screen()
screen.setup(1000, 800)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

#scale
max_value = max(
    np.max(np.abs(shape)),
    np.max(np.abs(translated)),
    np.max(np.abs(rotated)),
    np.max(np.abs(scaled)),
    abs(cx),
    abs(cy),
    1
)
scale = 300 / max_value
# -----------------------
# Draw X-axis
# -----------------------

t.pencolor("gray")

t.penup()
t.goto(-400, 0)
t.pendown()
t.goto(400, 0)
t.write("X", font=("Arial", 14))


# -----------------------
# Draw Y-axis
# -----------------------

t.penup()
t.goto(0, -300)
t.pendown()
t.goto(0, 300)
t.write("Y", font=("Arial", 14))

#draw center point
t.pencolor("green")
t.penup()
t.goto(cx*scale, cy*scale)
t.dot(10)

#show original triangle
t.pencolor("black")
x, y = shape[0]
t.penup()
t.goto(x*scale, y*scale)
t.pendown()
for x,y in shape[1:]:
    t.goto(x*scale, y*scale)

#show translated triangle
t.pencolor("blue")
x, y = translated[0]
t.penup()
t.goto(x*scale, y*scale)
t.pendown()
for x,y in translated[1:]:
    t.goto(x*scale, y*scale)

#show rotated triangle 
t.pencolor("red")
x, y = rotated[0]
t.penup()
t.goto(x*scale, y*scale)
t.pendown()
for x,y in rotated[1:]:
    t.goto(x*scale, y*scale)   

#show scalled triangle
t.pencolor("purple")
x, y = scaled[0]
t.penup()
t.goto(x*scale, y*scale)
t.pendown()
for x,y in scaled[1:]:
    t.goto(x*scale, y*scale)

turtle.done()
