from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('1000x500')
window.title('Time')
window.resizable(False,False)
window['bg']='gray'

def products():
    products_label_number['text']=int(products_label_number['text'])+int(products_entry.get())
def cloth():
    cloth_label_number['text']=int(cloth_label_number['text'])+int(cloth_entry.get())
def cafe():
    cafe_label_number['text']=int(cafe_label_number['text'])+int(cafe_entry.get())
def subscription():
    subscription_label_number['text']=int(subscription_label_number['text'])+int(subscription_entry.get())
def transport():
    transport_label_number['text']=int(transport_label_number['text'])+int(transport_entry.get())

products_label = Label(text='Продукти',fg='orange',bg='gray',font='sanscript 30')
products_label.place(x=10,y=10)

products_entry = Entry(fg='orange',font='sanscript 30',bg='gray',width=8)
products_entry.place(x=10,y=75)

products_button = Button(command=products,text='Додати',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2')
products_button.place(x=10,y=150)

products_label_number = Label(text='0',fg='orange',bg='gray',font='sanscript 30')
products_label_number.place(x=10,y=250)


cloth_label = Label(text='Одяг',fg='orange',bg='gray',font='sanscript 30')
cloth_label.place(x=200,y=10)

cloth_entry = Entry(fg='orange',font='sanscript 30',bg='gray',width=8)
cloth_entry.place(x=200,y=75)

cloth_button = Button(command=cloth,text='Додати',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2')
cloth_button.place(x=200,y=150)

cloth_label_number = Label(text='0',fg='orange',bg='gray',font='sanscript 30')
cloth_label_number.place(x=200,y=250)


cafe_label = Label(text='Кафе та\nресторани',fg='orange',bg='gray',font='sanscript 20')
cafe_label.place(x=400,y=10)

cafe_entry = Entry(fg='orange',font='sanscript 30',bg='gray',width=8)
cafe_entry.place(x=400,y=75)

cafe_button = Button(command=cafe,text='Додати',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2')
cafe_button.place(x=400,y=150)

cafe_label_number = Label(text='0',fg='orange',bg='gray',font='sanscript 30')
cafe_label_number.place(x=400,y=250)


subscription_label = Label(text='Підписки',fg='orange',bg='gray',font='sanscript 30')
subscription_label.place(x=600,y=10)

subscription_entry = Entry(fg='orange',font='sanscript 30',bg='gray',width=8)
subscription_entry.place(x=600,y=75)

subscription_button = Button(command=subscription,text='Додати',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2')
subscription_button.place(x=600,y=150)

subscription_label_number = Label(text='0',fg='orange',bg='gray',font='sanscript 30')
subscription_label_number.place(x=600,y=250)


transport_label = Label(text='Транспорт',fg='orange',bg='gray',font='sanscript 30')
transport_label.place(x=800,y=10)

transport_entry = Entry(fg='orange',font='sanscript 30',bg='gray',width=8)
transport_entry.place(x=800,y=75)

transport_button = Button(command=transport,text='Додати',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2')
transport_button.place(x=800,y=150)

transport_label_number = Label(text='0',fg='orange',bg='gray',font='sanscript 30')
transport_label_number.place(x=800,y=250)


window.mainloop()