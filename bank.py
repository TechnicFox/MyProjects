from tkinter import *
from tkinter import messagebox
import time

window = Tk()
window.geometry('500x500')
window.title('Time')
window.resizable(False,False)
window['bg']='gray'

def plus():
    money['text']=int(money['text'])+1
def minus():
    money['text']=int(money['text'])-1
def some():
    money['text']=int(money['text'])-int(entry_years.get())


money = Label(text='0',fg='orange',font='sanscript 30',bg='gray')
money.place(x=230,y=100)

Bank = Label(text='Hacked bank™️',fg='orange',font='sanscript 30',bg='gray')
Bank.place(x=100,y=10)

button_minus = Button(command=minus,text='-',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2')
button_minus.place(x=100,y=400)

button_place = Button(command=plus,text='+',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2')
button_place.place(x=300,y=400)

entry_years = Entry(fg='orange',font='sanscript 30',bg='gray',justify='center',width=8)
entry_years.place(x=150,y=260)
entry_years.insert(0,'0')

button_do = Button(command=some,text='?',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2')
button_do.place(x=200,y=400)

heck = Label(text='You hecked ',fg='orange',font='sanscript 30',bg='gray')
heck.place(x=50,y=200)

entry_ha = Entry(fg='orange',font='sanscript 30',bg='gray',justify='left',width=8)
entry_ha.place(x=280,y=200)
entry_ha.insert(0,'')


window.mainloop()