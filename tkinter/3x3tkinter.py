from tkinter import *
from tkinter import messagebox
import random

def exit_(event):
    window.destroy()
def help(event):
    messagebox.showinfo('INFO','F1-INFO\nF12-New game\nESC-Exit')
def begin(event):
    global butn
    global field
    global numButton
    for b in butn:
        b.config(bg='green',text='')
    field = [0,0,0,0,0,0,0,0,0]
    numButton=[]
def logic():
    global field
    global numButton
    if len(numButton)==9:
        messagebox.showinfo('INFO','DRAW')
    else:
        end = False
        if field[0]==field[1]==field[2]:
            winner = field[0]
            end=True
        elif field[3]==field[4]==field[5]:
            winner = field[3]
            end=True
        elif field[6]==field[7]==field[8]:
            winner = field[6]
            end=True
        elif field[0]==field[3]==field[6]:
            winner = field[0]
            end=True
        elif field[1]==field[4]==field[7]:
            winner = field[3]
            end=True
        elif field[2]==field[5]==field[8]:
            winner = field[6]
            end=True
        elif field[0]==field[4]==field[8]:
            winner = field[3]
            end=True
        elif field[2]==field[4]==field[6]:
            winner = field[6]
            end=True
        if end:
            if winner==1:
                user='0'
            elif winner==2:
                user='X'
            messagebox.showinfo('INFO',f'{user} WON!')
        begin(None)
def click(butn,num):
    global numButton
    if num not in numButton:
        global X0
        if X0 == 1:
            butn['text']='0'
            butn.config(bg='blue')
            field[num]=X0
            X0=2
        else:
            butn['text']='X'
            butn.config(bg='red')
            field[num]=X0
            X0=1
        numButton.append(num)
        logic()

field=[0,0,0,0,0,0,0,0,0]
X0 = 2
numButton=[]

window = Tk()
window.geometry('346x304')
window.title('3X3')
window.resizable(False,False)
window['bg']='gray'

button_q = Button(text='',font='sanscript 15',bg='gray',activeforeground='black',activebackground='gray',cursor='hand2',width=15,height=6,command=lambda:click(butn[0],0))
button_q.place(x=0,y=0)
button_w = Button(text='',font='sanscript 100',bg='gray',activeforeground='black',activebackground='gray',cursor='hand2',width=15,height=6,command=lambda:click(butn[1],1))
button_w.place(x=115,y=0)
button_e = Button(text='',font='sanscript 100',bg='gray',activeforeground='black',activebackground='gray',cursor='hand2',width=15,height=6,command=lambda:click(butn[2],2))
button_e.place(x=230,y=0)
button_a = Button(text='',font='sanscript 100',bg='gray',activeforeground='black',activebackground='gray',cursor='hand2',width=15,height=6,command=lambda:click(butn[3],3))
button_a.place(x=0,y=101)
button_s = Button(text='',font='sanscript 100',bg='gray',activeforeground='black',activebackground='gray',cursor='hand2',width=15,height=6,command=lambda:click(butn[4],4))
button_s.place(x=115,y=101)
button_d = Button(text='',font='sanscript 100',bg='gray',activeforeground='black',activebackground='gray',cursor='hand2',width=15,height=6,command=lambda:click(butn[5],5))
button_d.place(x=230,y=101)
button_z = Button(text='',font='sanscript 100',bg='gray',activeforeground='black',activebackground='gray',cursor='hand2',width=15,height=6,command=lambda:click(butn[6],6))
button_z.place(x=0,y=202)
button_x = Button(text='',font='sanscript 100',bg='gray',activeforeground='black',activebackground='gray',cursor='hand2',width=15,height=6,command=lambda:click(butn[7],7))
button_x.place(x=115,y=202)
button_c = Button(text='',font='sanscript 100',bg='gray',activeforeground='black',activebackground='gray',cursor='hand2',width=15,height=6,command=lambda:click(butn[8],8))
button_c.place(x=230,y=202)

butn = [button_q,button_w,button_e,button_a,button_s,button_d,button_z,button_x,button_c]

window.bind('<Escape>',exit_)
window.bind('<F1>',help)
window.bind('<F12>',begin)

window.bind('<q>',lambda e:click(butn[0],0))
window.bind('<w>',lambda e:click(butn[1],1))
window.bind('<e>',lambda e:click(butn[2],2))
window.bind('<a>',lambda e:click(butn[3],3))
window.bind('<s>',lambda e:click(butn[4],4))
window.bind('<d>',lambda e:click(butn[5],5))
window.bind('<z>',lambda e:click(butn[6],6))
window.bind('<x>',lambda e:click(butn[7],7))
window.bind('<c>',lambda e:click(butn[8],8))

window.mainloop()