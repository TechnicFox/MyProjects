from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('500x1000')
window.title('Time')
window.resizable(False,False)
window['bg']='gray'

# def range_num():
#     y = 10
#     for i in range(int(min.get()),int(max.get())+1):
#         number = Label(text=f'{i}',fg='orange',bg='gray',font='sanscript 20')
#         number.place(x=300,y=y)
#         y+=30

# min = Entry(fg='orange',font='sanscript 30',bg='gray',width=8)
# min.place(x=10,y=10)

# max = Entry(fg='orange',font='sanscript 30',bg='gray',width=8)
# max.place(x=10,y=100)

# products_button = Button(command=range_num,text='range',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2')
# products_button.place(x=10,y=200)

def range_num():
    sum = 0
    for i in range(int(max.get())):
        if i%3==0 or i%5==0:
            sum+=i
    number['text']=sum
max = Entry(fg='orange',font='sanscript 30',bg='gray',width=8)
max.place(x=10,y=100)

products_button = Button(command=range_num,text='range',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2')
products_button.place(x=10,y=200)

number = Label(text='0',fg='orange',bg='gray',font='sanscript 20')
number.place(x=300,y=10)

window.mainloop()

