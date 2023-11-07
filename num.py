from tkinter import *
from random import *

window = Tk()
window.geometry('600x600')
window.title('🎲')
window['bg']='aqua'

label3 = Label(text='✅',fg='blue',font='sanscript 15',bg='aqua')

num = randint(1,11)
def big_small():
    label3['text'] = ''
    if int(entry.get()) > num:
        label2['text']='📉📉'
    elif int(entry.get()) < num:
        label2['text'] = '📈📈'
    else:
        label2['text'] = '✅✅'

label1 = Label(text='Enter number:',fg='blue',font='sanscript 20',bg='aqua')
label1.pack()

entry = Entry(bg='aqua',font='sanscript 20',fg='blue')
entry.pack()

button = Button(command=big_small,text='❓Check❓',fg='blue',font='sanscript 40',bg='aqua',activebackground='aqua',activeforeground='blue',borderwidth=0,cursor='cross')
button.pack()

label2 = Label(text='',fg='blue',font='sanscript 20',bg='aqua')
label2.pack()

def show():
    num = randint(int(entry_A.get()),int(entry_B.get())+1)
    label3['text']='✅'
    label3.place(x=285,y=500)
    label2['text'] = ''

entry_A = Entry(bg='aqua',font='sanscript 15')
entry_A.place(x=20,y=560)
entry_B = Entry(bg='aqua',font='sanscript 15')
entry_B.place(x=350,y=560)
button = Button(command=show,text='Set',fg='blue',font='sanscript 15',bg='aqua',activebackground='aqua',activeforeground='blue',borderwidth=0,cursor='cross')
button.place(x=280,y=555)



window.mainloop()