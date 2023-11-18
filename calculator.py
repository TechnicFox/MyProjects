from tkinter import *
from tkinter import messagebox
import random



window = Tk()
window.geometry('243x400')
window.title('3X3')
window.resizable(False,False)
window['bg']='gray'

def count():
    ans=str(eval(entry.get()))
    entry.delete(0,END)
    entry.insert(0,ans)

entry = Entry(text='',fg='orange',font='sanscript 50',bg='gray',width=7,justify='right',insertwidth=1,cursor='hand2')
entry.place(x=-20,y=0)

button_1 = Button(text='1',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1,command=lambda:entry.insert(END,1))
button_1.place(x=2,y=80)
button_2 = Button(text='2',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1,command=lambda:entry.insert(END,2))
button_2.place(x=59,y=80)
button_3 = Button(text='3',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1,command=lambda:entry.insert(END,3))
button_3.place(x=116,y=80)

button_4 = Button(text='4',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1,command=lambda:entry.insert(END,4))
button_4.place(x=2,y=160)
button_5 = Button(text='5',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1,command=lambda:entry.insert(END,5))
button_5.place(x=59,y=160)
button_6 = Button(text='6',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1,command=lambda:entry.insert(END,6))
button_6.place(x=116,y=160)

button_7 = Button(text='7',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1,command=lambda:entry.insert(END,7))
button_7.place(x=2,y=240)
button_8 = Button(text='8',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1,command=lambda:entry.insert(END,8))
button_8.place(x=59,y=240)
button_9 = Button(text='9',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1,command=lambda:entry.insert(END,9))
button_9.place(x=116,y=240)

button_0 = Button(text='0',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1,command=lambda:entry.insert(END,0))
button_0.place(x=59,y=320)

button_multi = Button(text='*',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=3,height=1,command=lambda:entry.insert(END,'*'))
button_multi.place(x=171,y=160)
button_add = Button(text='+',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=3,height=1,command=lambda:entry.insert(END,'+'))
button_add.place(x=171,y=80)
button_equal = Button(text='=',font='sanscript 40',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=2,command=count)
button_equal.place(x=171,y=240)

button_minus = Button(text='-',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1,command=lambda:entry.insert(END,'-'))
button_minus.place(x=116,y=320)

button_divide = Button(text='/',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2',width=2,height=1,command=lambda:entry.insert(END,'/'))
button_divide.place(x=2,y=320)




window.mainloop()
