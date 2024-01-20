from turtle import *

v = 100
st = 15
color('blue')
width(5)
shape('circle')
speed(v)
def draw(x,y):
    goto(x,y)

def set_red():
    color('red')
def set_green():
    color('green')
def set_yellow():
    color('yellow')
def set_blue():
    color('blue')
def set_purple():
    color('purple')
def set_orange():
    color('orange')

def step_up():
    goto(xcor(),ycor()+st)
def step_down():
    goto(xcor(),ycor()-st)
def step_right():
    goto(xcor()+st,ycor())
def step_left():
    goto(xcor()-st,ycor())

def start():
    begin_fill()
def end():
    end_fill()

def square():
    for i in range(0,4):
        forward(500)
        right(90)
def triangle():
    for i in range(0,3):
        forward(500)
        right(120)
def circle_super():
    circle(100)


keyboard = getscreen()
keyboard.onkey(set_red, 'r')
keyboard.onkey(set_green, 'g')
keyboard.onkey(set_yellow, 'y')
keyboard.onkey(set_blue, 'b')
keyboard.onkey(set_purple, 'p')
keyboard.onkey(set_orange, 'o')

keyboard.onkey(step_up, 'Up')
keyboard.onkey(step_down, 'Down')
keyboard.onkey(step_right, 'Right')
keyboard.onkey(step_left, 'Left')

keyboard.onkey(start, '`')
keyboard.onkey(end, 'BackSpace')

keyboard.onkey(circle_super, 'c')
keyboard.onkey(triangle, 't')
keyboard.onkey(square, 's')


keyboard.listen()

done()


