from turtle import *
from random import *
import time
import turtle


window = Screen()
window.title('Ping Pong⚫')
window.bgcolor('blue')
window.setup(width=1.0, height=1.0)
window.tracer(0)

border = Turtle()
border.hideturtle()
border.speed(0)
border.color('green')
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()
border.goto(0, 300)
border.color('white')
border.setheading(270)
for i in range(26):
    if i % 2 == 0:
        border.forward(24)
    else:
        border.penup()
        border.forward(24)
        border.pendown()


rocketA = turtle.Turtle()
rocketA.color(input('Enter color for player A>>>'))
rocketA.shape('square')
rocketA.shapesize(stretch_len=1, stretch_wid=5)
rocketA.penup()
rocketA.goto(-450, 0)

rocketB = turtle.Turtle()
rocketB.color(input('Enter color for player B>>>'))
rocketB.shape('square')
rocketB.shapesize(stretch_len=1, stretch_wid=5)
rocketB.penup()
rocketB.goto(450, 0)
window.tracer(0)

font = ('Arial', 44)
scoreA=-1
sa = Turtle()
sa.hideturtle()
sa.penup()
sa.color('white')
sa.goto(-200, 300)
sa.write(scoreA, font=font)

scoreB=0
sb = Turtle()
sb.hideturtle()
sb.penup()
sb.color('white')
sb.goto(200, 300)
sb.write(scoreB, font=font)

screen = turtle.Screen()

def move_up_A():
    y = rocketA.ycor()+20
    if y > 250:
        y = 250
    rocketA.sety(y)

def move_down_A():
    y = rocketA.ycor()-20
    if y < -250:
        y = -250
    rocketA.sety(y)
def move_up_B():
    y = rocketB.ycor()+20
    if y > 250:
        y = 250
    rocketB.sety(y)
def move_down_B():
    y = rocketB.ycor()-20
    if y < -250:
        y = -250
    rocketB.sety(y)

playerA_move_up = False
playerA_move_down = False
playerB_move_up = False
playerB_move_down = False

def set_playerA_move_up():
    global playerA_move_up
    playerA_move_up = True

def set_playerA_move_down():
    global playerA_move_down
    playerA_move_down = True

def set_playerB_move_up():
    global playerB_move_up
    playerB_move_up = True

def set_playerB_move_down():
    global playerB_move_down
    playerB_move_down = True

# Functions to clear flags when keys are released
def clear_playerA_move_up():
    global playerA_move_up
    playerA_move_up = False

def clear_playerA_move_down():
    global playerA_move_down
    playerA_move_down = False

def clear_playerB_move_up():
    global playerB_move_up
    playerB_move_up = False

def clear_playerB_move_down():
    global playerB_move_down
    playerB_move_down = False

# Bind keys to functions
screen.onkeypress(set_playerA_move_up, 'w')
screen.onkeypress(set_playerA_move_down, 's')
screen.onkeypress(set_playerB_move_up, 'Up')
screen.onkeypress(set_playerB_move_down, 'Down')

screen.onkeyrelease(clear_playerA_move_up, 'w')
screen.onkeyrelease(clear_playerA_move_down, 's')
screen.onkeyrelease(clear_playerB_move_up, 'Up')
screen.onkeyrelease(clear_playerB_move_down, 'Down')

screen.listen()


ball = Turtle()
ball.shape('circle')
ball.speed(0)
ball.color('black')
ball.dx = 0.6
ball.dy = -0.6
ball.penup()
winer = Turtle()
winer.color('red')
winer.hideturtle()
winer.penup()
winer.goto(-200, -25)
winer.pendown
while True:
    window.update()

    if playerA_move_up:
        y = rocketA.ycor()+0.60
        if y > 250:
            y = 250
        rocketA.sety(y)
    if playerA_move_down:
        y = rocketA.ycor()-0.60
        if y < -250:
            y = -250
        rocketA.sety(y)
    if playerB_move_up:
        y = rocketB.ycor()+0.60
        if y > 250:
            y = 250
        rocketB.sety(y)
    if playerB_move_down:
        y = rocketB.ycor()-0.60
        if y < -250:
            y = -250
        rocketB.sety(y)

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() >= 290:
        ball.dy = -ball.dy
    if ball.ycor() <= -290:
        ball.dy = -ball.dy
    if ball.xcor() >= 490:
        scoreA += 1
        sa.clear()
        sa.write(scoreA, font=font)
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-0.5,0.6,0.5,0.3,0.4,-0.3,])
        ball.dy = choice([-0.5,0.6,0.5,0.3,0.4,-0.3,])
    if ball.xcor() <= -490:
        scoreB += 1
        sb.clear()
        sb.write(scoreB, font=font)
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-0.5,0.6,0.5,0.3,0.4,-0.3,])
        ball.dy = choice([-0.5,0.6,0.5,0.3,0.4,-0.3,])
    if (ball.dx > 0) and (rocketB.xcor()-10<=ball.xcor()<=rocketB.xcor()+10) and (rocketB.ycor()-50<=ball.ycor()<=rocketB.ycor()+50):
        ball.dx = -ball.dx
    if (ball.dx < 0) and (rocketA.xcor()-10<=ball.xcor()<=rocketA.xcor()+10) and (rocketA.ycor()-50<=ball.ycor()<=rocketA.ycor()+50):
        ball.dx = -ball.dx
    if scoreA >= 20:
        winer.write('Left Wins🎉🎉🎉', font=font)
        break
    if scoreB >= 20:
        winer.write('Right Wins🎉🎉🎉', font=font)
        break


window.mainloop()