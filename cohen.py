#import
import turtle

#rectangle
xmin, ymin = -100, -50
xmax, ymax = 300, 200

#sample line
x1, y1 = -180, -30
x2, y2 = 300, 300

#regional code
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

#compute code
def compute_code(x, y):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code                

#cohen sutherland
def cohen_sutherland(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)

    while True:
        #both inside the window
        if code1 == 0 & code2 == 0:
            return True,(x1, y1, x2, y2)
        #both completely outside the window
        if code1 & code2:
            return False, None
        #choose outside code
        code_out = code1 if code1 != 0 else code2

        if code_out & TOP:
            if y2 == y1:
                return False, None
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax   
        elif code_out & BOTTOM:
            if y2 == y1:
                return False, None
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin
        elif code_out & RIGHT:
            if x2 == x1:
                return False, None
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            x = xmax     
        else:
            if x2 == x1:
                return False, None
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin
        #replace outside code
        if code_out == code1:
            x1, y1 = x, y
            code1 = compute_code(x1, y1)
        else:
            x2, y2 = x, y1
            code2 = compute_code(x2, y2)         

#call algo
accepted, clipped = cohen_sutherland(
    x1, y1,
    x2, y2,
)
if accepted:
    print("Clipped Line : ", clipped)
else:
    print("Completely outside the window.")    

#turtle visualization start
screen = turtle.Screen()
screen.setup(1000, 800)
screen.title("Cohen sutherland")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

#scale
values = [
    xmin, ymin,
    xmax, ymax,
    x1, y1,
    x2, y2
]
max_value = max(
    max(abs(v) for v in values),
    1
)
scale = 250 / max_value

#draw x axis
t.pencolor("gray")

t.penup()
t.goto(-400, 0)
t.pendown()
t.goto(400, 0)

t.write("X", font=("Arial", 14))


#draw y axis
#t.pencolor("gray")

t.penup()
t.goto(0, -300)
t.pendown()
t.goto(0, 300)

t.write("Y", font=("Arial", 14))


#draw rectangle
t.pencolor("green")
t.pensize(3)

t.penup()
t.goto(xmin * scale, ymin * scale)
t.pendown()

t.goto(xmax * scale, ymin * scale)
t.goto(xmax * scale, ymax * scale)
t.goto(xmin * scale, ymax * scale)
t.goto(xmin * scale, ymin * scale)


#draw sample line
t.pencolor("red")
t.pensize(1)

t.penup()
t.goto(x1 * scale, y1 * scale)
t.pendown()

t.goto(x2 * scale, y2 * scale)

#draw original line
if accepted:

    cx1, cy1, cx2, cy2 = clipped

    t.pencolor("blue")
    t.pensize(5)

    t.penup()
    t.goto(cx1 * scale, cy1 * scale)
    t.pendown()

    t.goto(cx2 * scale, cy2 * scale)


turtle.done()
