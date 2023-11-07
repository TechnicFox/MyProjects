from turtle import *
import time
import random

window = Screen()
window.setup(width=600,height=600)
window.bgcolor('green')
window.title('Snake.io🐍🐍🐍')
window.tracer(0)

delay=0.1
score=0
high_score=0

head = Turtle()
head.shape('square')
head.color('white')
head.penup()
head.goto(0,0)
head.direction = 'Stop'

apple = Turtle()
shapes = random.choice(['triangle','circle','square'])
colors = random.choice(['red','purple','yellow','orange'])
apple.shape(shapes)
apple.color(colors)
apple.speed(0)
head.penup()
head.goto(0,100)

text = Turtle()
def text_update():
    text.clear()
    text.goto(-295,270)
    text.write(f'Score: {score}',font=font)
    text.goto(-295,245)
    text.write(f'High score: {high_score}',font=font)
text.color('lime')
text.penup()
text.hideturtle()
text.speed(0)
font = ('Arial',20,'bold')
text_update()

def go_up():
    if head.direction != 'Down':
        head.direction = 'Up'
def go_down():
    if head.direction != 'Up':
        head.direction = 'Down'
def go_left():
    if head.direction != 'Right':
        head.direction = 'Left'
def go_right():
    if head.direction != 'Left':
        head.direction = 'Right'

def move():
    if head.direction == 'Up':
        head.sety(head.ycor()+20)
    if head.direction == 'Down':
        head.sety(head.ycor()-20)
    if head.direction == 'Right':
        head.setx(head.xcor()+20)
    if head.direction == 'Left':
        head.setx(head.xcor()-20)

window.listen()
window.onkeypress(go_up, 'Up')    
window.onkeypress(go_down,'Down')  
window.onkeypress(go_left,'Left')  
window.onkeypress(go_right,'Right')

segments = []

def reset(score,delay):
    time.sleep(1)
    head.goto(0,0)
    head.direction = "Stop"
    for i in segments:
        i.goto(1000,1000)
    score = 0
    delay = 0.1
    text_update()
    return score,delay

def apple_reset(apple):
    x = random.randint(-270,270)
    y = random.randint(-270,270)
    apple.penup()
    apple.goto(x,y)
    shapes = random.choice(['triangle','circle','square'])
    colors = random.choice(['red','purple','yellow','orange'])
    apple.shape(shapes)
    apple.color(colors)
    apple.pendown()

while True:
    window.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:   
        score,delay = reset(score,delay)
    if head.distance(apple)<20:
        apple_reset(apple)
        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('blue')
        new_segment.penup()
        segments.append(new_segment)
        score += 1
        if score %10==0:
            head.color(colors)
        text_update()
        time.sleep(delay)
    if score > high_score:
        high_score = score
        text_update()
    for j in range(len(segments)-1,0,-1):
        x = segments[j-1].xcor()
        y = segments[j-1].ycor()
        segments[j].goto(x,y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()
    for k in segments:
        if k.distance(head) < 20:
            score,delay = reset(score,delay)
    time.sleep(delay)
window.mainloop()


