from turtle import *
from random import *
import sys
import time

window = Screen()
window.setup(width=300,height=300)
window.bgcolor('white')
window.title('Cube1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣')
window.tracer(1)

dotposition = [
    [(0,0,'black'),(-100,100,'white'),(-100,0,'white'),(-100,-100,'white'),(100,100,'white'),(100,0,'white'),(100,-100,'white')],
    [(0,0,'white'),(-100,100,'black'),(-100,0,'white'),(-100,-100,'white'),(100,100,'white'),(100,0,'white'),(100,-100,'black')],
    [(0,0,'black'),(-100,100,'black'),(-100,0,'white'),(-100,-100,'white'),(100,100,'white'),(100,0,'white'),(100,-100,'black')],
    [(0,0,'white'),(-100,100,'black'),(-100,0,'white'),(-100,-100,'black'),(100,100,'black'),(100,0,'white'),(100,-100,'black')],
    [(0,0,'black'),(-100,100,'black'),(-100,0,'white'),(-100,-100,'black'),(100,100,'black'),(100,0,'white'),(100,-100,'black')],
    [(0,0,'white'),(-100,100,'black'),(-100,0,'black'),(-100,-100,'black'),(100,100,'black'),(100,0,'black'),(100,-100,'black')]
]
dot = [Turtle() for i in range(7)]

in_row_5 = 0
in_row_6 = 0
in_row_1 = 0

def click():
    num = randint(1,6)
    global in_row_5
    global in_row_6
    global in_row_1

    if num == 5: 
        in_row_5 += 1
        in_row_6 = 0

    elif num == 6:
        in_row_6 += 1
        in_row_5 = 0

    elif num == 1:
        in_row_1 += 1

    else:
        in_row_1 = 0

    if in_row_1 == 2:
        hideturtle()
        penup()
        goto(-100,20)
        pendown()
        color('red')
        write('You Lose!😭', font='Arial 30')
        time.sleep(5)
        sys.exit()
        

    if in_row_5 == 3 or in_row_6 == 3:
        hideturtle()
        penup()
        goto(-90,20)
        pendown()
        color('red')
        write('You Win!🎉', font='Arial 30')
        time.sleep(5)
        sys.exit()

    for i in range(7):
        dot[i].shape('circle')
        dot[i].color(dotposition[num-1][i][2])
        dot[i].penup()
        dot[i].goto(dotposition[num-1][i][0],dotposition[num-1][i][1])
        dot[i].dot()


keyboard = getscreen()
keyboard.onkeypress(click, 'space')
keyboard.listen()

done()