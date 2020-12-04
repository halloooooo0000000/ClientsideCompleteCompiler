import turtle
f = turtle
f.pencolor("white")
f.speed(1000)
f.penup()
f.goto(-250, 200)
f.pendown()
for x in range(2): # makes overall flag rectangle
    f.forward(570) # 300*1.9
    f.right(90)
    f.forward(300)
    f.right(90)
f.penup()
f.goto(-22, 200)  # 2/5 of 570
f.pendown()
f.fillcolor("#051D5B")
f.begin_fill()
f.right(90)
f.forward((300/13)*7) # height of blue
f.right(90)
f.forward(228)
f.penup()
f.right(90)
f.forward((300/13)*7)
f.right(90)
f.forward(228)
f.end_fill()
for x in range(4):
    f.fillcolor("#A82019")
    f.begin_fill()
    f.forward(342)  # 570/5 *3
    f.right(90)
    f.forward(300/13)  # 300/13
    f.right(90)
    f.pendown()
    f.forward(342)
    f.penup()
    f.right(90)
    f.forward(300 / 13)
    f.end_fill()
    f.back((300/13)*2)
    f.right(90)
f.back(228)
for x in range(3):
    f.fillcolor("#A82019")
    f.begin_fill()
    f.forward(570)  # 570/5 *3
    f.right(90)
    f.forward(300 / 13)  # 300/13
    f.right(90)
    f.pendown()
    f.forward(570)
    f.penup()
    f.right(90)
    f.forward(300 / 13)
    f.end_fill()
    f.back((300 / 13) * 2)
    f.right(90)
#f.goto(-230,180)
f.fillcolor("white")
f.goto(-240.23, 184.8462) #diameter of star / 2 also take into consideration lenth of variables H&F
f.pendown()
for x in range(6):
    for x in range(5):
        for x in range(5):
            f.begin_fill()
            f.forward(18.46)
            f.right(144)
        f.end_fill()

        f.penup()
        f.right(90)
        f.forward((300/13)*7 / 5)
        f.left(90)
        f.pendown()
    f.penup()
    f.left(90)
    f.forward((300/13)*7)
    f.right(90)
    f.forward(228/6)
    f.pendown()


f.penup()
f.goto(-221.32, 168.6924)
f.pendown()

for x in range(5):
    for x in range(4):
        for x in range(5):
            f.begin_fill()
            f.forward(18.46)
            f.right(144)
        f.end_fill()

        f.penup()
        f.right(90)
        f.forward(32)
        f.left(90)
        f.pendown()
    f.penup()
    f.left(90)
    f.forward(129)
    f.right(90)
    f.forward(38)
    f.pendown()

f.done()