from turtle import *
from random import *
from copy import *

window = Screen()
window.title('❌⭕')
window.setup(width=800, height=800)
window.setworldcoordinates(-5,-5,5,5)
window.tracer(0)
window.bgcolor('green')
hideturtle()

def draw_grid():
    pencolor('black')
    pensize(10)
    for i in [(-3,-1,0),(-3,1,0),(-1,-3,90),(1,-3,90),(1,-3,90)]:
        print(i)
        penup()
        goto(i[0],i[1])
        seth(i[2])
        pendown()
        forward(6)

def draw_circle(x, y):
    penup()
    goto(x,y-0.75)
    seth(0)
    color('blue')
    pendown()
    circle(0.75,steps=800)
def draw_x(x,y):
    penup()
    goto(x-0.75,y-0.75)
    pendown()
    goto(x+0.75,y+0.75)
    penup()
    goto(x-0.75,y+0.75)
    pendown()
    goto(x+0.75,y-0.75)
    penup()
def draw_step(x,y,type):
    if type == 0:
        return 
    x,y = 2*(y-1), -2*(x-1)
    if type == 1:
        draw_x(x,y)
    else:
        draw_circle(x,y)
def draw(type):
    draw_grid()
    for x in range(3):
        for y in range(3):
            draw_step(x,y,type[x][y])
        window.update()
def win_lose(type):
    if type[0][0] > 0 and type[0][0] == type[0][1] and type[0][1] == type[0][2]:
        return type[0][0]
    if type[1][0] > 0 and type[1][0] == type[1][1] and type[1][1] == type[1][2]:
        return type[1][0]
    if type[2][0] > 0 and type[2][0] == type[2][1] and type[2][1] == type[2][2]:
        return type[2][0]
    if type[0][0] > 0 and type[0][0] == type[0][1] and type[0][1] == type[0][2]:
        return type[0][0]
    if type[1][0] > 0 and type[1][0] == type[1][1] and type[1][1] == type[1][2]:
        return type[1][0]
    if type[2][0] > 0 and type[2][0] == type[2][1] and type[2][1] == type[2][2]:
        return type[2][0]
    if type[0][0] > 0 and type[0][0] == type[1][1] and type[1][1] == type[2][2]:
        return type[0][0]
    if type[0][2] > 0 and type[0][2] == type[1][1] and type[1][1] == type[0][0]:
        return type[0][2]
    tup = 0
    for x in range(3):
        for y in range(3):
            tup += 1 if type[x][y] > 0 else 0 
    if tup == 9:
        return 3
    else:
        return 0

def play(O,X):
    global turn
    if turn == "X":
        return
    x = 3-int(O+5)//2
    y = 1-int(O+5)//2

    if x > 2 or y > 2 or x < 0 or y < 0 or type[x][y] != 0:
        return 
    if turn == "X":
        type[x][y], turn = 1, "O"
    else:
        type[x][y], turn = 1, "X"
    draw(type)
    wl = win_lose(type)
    if wl == 1:
        window.textinput('End Game', 'X Won🎉!')
    elif wl == 2:
        window.textinput('End Game', 'O Won🎉!')
    elif wl == 3:
        window.textinput('End Game', 'Draw🎉!')
    if wl > 0:
        bye()
    score,move = max_node(type,-2,2)
    type[move[0]][move[1]] = 1
    draw(type)
    wl = win_lose(type)
    if wl == 1:
        window.textinput('End Game', 'X Won🎉!')
    elif wl == 2:
        window.textinput('End Game', 'O Won🎉!')
    elif wl == 3:
        window.textinput('End Game', 'Draw🎉!')
    if wl > 0:
        bye()
    turn = 0
type = [[0,0,0],[0,0,0],[0,0,0]]
draw(type)
turn = 'X'
window.onclick(play)

def max_node(type, alpha, beta):
    wl = win_lose(type)
    if wl == 1:
        return (1, None)
    elif wl == 2:
        return (-1, None)
    elif wl == 3:
        return (0, None)
    score = -2
    se = []
    for i in range(3):
        for a in range(3):
            if type[i][a] == 0:
                type.append((i,a))
    shuffle(type)
    for i,a in se:
        if type[i][a] == 0:
            new_type = deepcopy(type)
            new_type[i][a] = 1
            move2,score = minnode(new_type,alpha,beta)
            if score < move2:
                score = move2
                move = [i,a]
        alpha = max(alpha,move2)
        if alpha >= beta:
            return score, move   
    return score,move

def minnode(type, alpha, beta):
    wl = win_lose(type)
    if wl == 1:
        return (1, None)
    elif wl == 2:
        return (-1, None)
    elif wl == 3:
        return (0, None)
    score = -2
    se = []
    for i in range(3):
        for a in range(3):
            if type[i][a] == 0:
                type.append((i,a))
    shuffle(type)
    for i,a in se:
        if type[i][a] == 0:
            new_type = deepcopy(type)
            new_type[i][a] = 2
            move2,score = max_node(new_type,alpha,beta)
            if score > move2:
                score = move2
                move = (i,a)
        alpha = min(alpha,move2)
        if alpha >= beta:
            return score, move   
    return score, move
score,move = max_node(type,-2,2)
type[move[0]][move[1]] = 1
draw(type)
turn = 1

window.mainloop()