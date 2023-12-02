from tkinter import *
from tkinter import messagebox
import time

window = Tk()
window.geometry('500x500')
window.title('Time')
window.resizable(False,False)
window['bg']='gray'

def calculate_money():
    mon = int(entry_money.get())
    per = int(entry_percent.get()[:-1])
    yer = int(entry_years.get())
    for i in range(yer):
        mon+=mon*(per/100)
    messagebox.showinfo('INFO',f'You will get: {round(mon)}')

money = Label(text='Money:',fg='orange',font='sanscript 30',bg='gray')
money.place(x=150,y=10)

entry_money = Entry(fg='orange',font='sanscript 30',bg='gray',justify='center',width=8)
entry_money.place(x=150,y=60)
entry_money.insert(0,'0')

percent = Label(text='Percent:',fg='orange',font='sanscript 30',bg='gray')
percent.place(x=150,y=110)

entry_percent = Entry(fg='orange',font='sanscript 30',bg='gray',justify='center',width=8)
entry_percent.place(x=150,y=160)
entry_percent.insert(0,'0%')

years = Label(text='Years:',fg='orange',font='sanscript 30',bg='gray')
years.place(x=150,y=210)

entry_years = Entry(fg='orange',font='sanscript 30',bg='gray',justify='center',width=8)
entry_years.place(x=150,y=260)
entry_years.insert(0,'0')

button_confirm = Button(command=calculate_money,text='Confirm',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2')
button_confirm.place(x=150,y=400)

print(int(entry_percent.get()[:-1]))
window.mainloop()