from tkinter import *
from tkinter import messagebox
import time

window = Tk()
window.geometry('300x300')
window.title('Time')
window.resizable(False,False)
window['bg']='gray'

timer = Label(text='00:00:00',fg='orange',font='sanscript 50',bg='gray')
timer.place(x=20,y=100)
entry = Entry(text='00:00:00',fg='orange',font='sanscript 40',bg='gray',justify='center',width=8)

active_timer = False

def set_timer():
    entry.delete(0,END)
    entry.insert(0,'00:00:00')
    timer.place_forget()
    button_start.place(x=100,y=200)
    entry.place(x=30,y=120)
def set_time():
    button_start.place_forget()
    entry.place_forget()
    timer.place(x=20,y=100)
def start():
    global active_timer
    active_timer = True

button_timer = Button(command=set_timer,text='Timer',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2')
button_timer.place(x=10,y=10)
button_time = Button(command=set_time,text='Time',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2')
button_time.place(x=170,y=10)
button_start = Button(command=start,text='Start',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2')


active_while = False
while True:
    if active_timer:
        time_set = entry.get()
        seconds = int(time_set[6:8])
        minutes = int(time_set[3:5])
        hours = int(time_set[0:2])
        active_timer =False
        active_while =True
        
    if active_while:
        time.sleep(1)
        entry.delete(0,END)
        entry.insert(0,f'{hours}:{minutes}:{seconds}')
        if seconds <= 0:
            minutes -=1
            seconds=59
        if minutes <= 0 and seconds <= 0:
            hours -=1
            minutes=59

        if entry.get()=='0:0:0':
            active_timer = False
            active_while = False
            messagebox.showinfo('INFO','Timer run out!')
            entry.delete(0,END)
            entry.insert(0,'00:00:00')

        seconds-=1


    timer['text']=time.strftime("%H:%M:%S")
    window.update()