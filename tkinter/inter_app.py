from tkinter import *



# label = Label(text='Hello world!',fg='red',font='sanscript 40', width=10, height=10,relief='groove')
# label.pack(side='bottom')


# entry = Entry(bg='purple',justify='right')
# entry.pack()

# def change_hi():
#     label['text']='hi world'


# text = Text(bg='purple')
# text.pack()

# button = Button(text='1+1',command=change_hi,bg='purple',fg='white', activebackground='pink')
# button.place(x=300,y=300)

window = Tk()
window.geometry('600x600')
window['bg']='aqua'

# label = Label(text='0', fg='blue',font='sanscript 40',bg='aqua')
# label.pack()

# def up():
#     label['text'] = int(label['text'])+1
# def down():
#     label['text'] = int(label['text'])-1
    

# button_plus = Button(command=up,text='+',fg='blue',font='sanscript 40',bg='aqua',activebackground='aqua',activeforeground='blue',borderwidth=0)
# button_plus.place(x=500,y=-20)
# button_minus = Button(command=down,text='-',fg='blue',font='sanscript 40',bg='aqua',activebackground='aqua',activeforeground='blue',borderwidth=0)
# button_minus.place(x=0,y=-20)

# import random

# def rand():
#     label['text']=(random.randint(1,6)+random.randint(1,6))

# button_plus = Button(command=rand,text='Generate',fg='blue',font='sanscript 40',bg='aqua',activebackground='aqua',activeforeground='blue',borderwidth=0)
# button_plus.pack(side='bottom')



# label = Label(text='',fg='blue',font='sanscript 40',bg='aqua',anchor='center')
# label.pack()

# entry = Entry(bg='aqua',font='sanscript 15')
# entry.place(y=20,x=200)

# def transform():
#     label['text']=str(round((int(entry.get())-32)*5/9))+' C°'

# button = Button(command=transform,text='Transform',fg='blue',font='sanscript 40',bg='aqua',activebackground='aqua',activeforeground='blue',borderwidth=0,cursor='cross')
# button.place(y=200,x=170)

# label = Label(text='',fg='blue',font='sanscript 40',bg='aqua')
# label.pack(side='bottom')

# text = Text(bg='blue',font='sanscript 15',cursor='watch')
# text.pack()

# def show():
#     for i in range(int(entry_A.get()),int(entry_B.get())+1):
#         Label(text=f'{i}',fg='blue',font='sanscript 40',bg='aqua').place(x=i*50,y=i*50)

# entry_A = Entry(bg='aqua',font='sanscript 15')
# entry_A.pack()
# entry_B = Entry(bg='aqua',font='sanscript 15')
# entry_B.pack()
# button = Button(command=show,text='press',fg='blue',font='sanscript 40',bg='aqua',activebackground='aqua',activeforeground='blue',borderwidth=0,cursor='cross')
# button.pack()

def show():
    sum = 0
    for i in range(int(entry_A.get())):
        if i % 3 == 0 or i % 5 == 0:
            sum+=i

    Label(text=f'{sum}',fg='blue',font='sanscript 40',bg='aqua').place(x=300,y=300)

entry_A = Entry(bg='aqua',font='sanscript 15')
entry_A.pack()
button = Button(command=show,text='press',fg='blue',font='sanscript 40',bg='aqua',activebackground='aqua',activeforeground='blue',borderwidth=0,cursor='cross')
button.pack()

window.mainloop()
