from tkinter import *
from tkinter import messagebox
import random



window = Tk()
window.geometry('243x400')
window.title('3X3')
window.resizable(False,False)
window['bg']='gray'

label = Entry(text='',fg='white',font='sanscript 50',bg='gray',width=7,justify='right',insertwidth=1,cursor='hand2')
label.place(x=-20,y=0)

button_1 = Button(text='1',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1)
button_1.place(x=2,y=80)
button_2 = Button(text='2',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1)
button_2.place(x=59,y=80)
button_3 = Button(text='3',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1)
button_3.place(x=116,y=80)

button_4 = Button(text='4',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1)
button_4.place(x=2,y=160)
button_5 = Button(text='5',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1)
button_5.place(x=59,y=160)
button_6 = Button(text='6',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1)
button_6.place(x=116,y=160)

button_7 = Button(text='7',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1)
button_7.place(x=2,y=240)
button_8 = Button(text='8',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1)
button_8.place(x=59,y=240)
button_9 = Button(text='9',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1)
button_9.place(x=116,y=240)


button_add = Button(text='+',font='sanscript 40',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=2)
button_add.place(x=230-59,y=80)
button_equal = Button(text='=',font='sanscript 40',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=2)
button_equal.place(x=230-59,y=240)

button_minus = Button(text='-',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1)
button_minus.place(x=175-59,y=320)
button_multi = Button(text='*',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1)
button_multi.place(x=118-59,y=320)
button_divide = Button(text='/',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1)
button_divide.place(x=61-59,y=320)




window.mainloop()
