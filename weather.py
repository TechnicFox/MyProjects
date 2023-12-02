from tkinter import *
from tkinter import messagebox
import time
import requests
from PIL import Image,ImageTk

API = '239d752fde52cd7ef542f755c2bd95cb'

window = Tk()
window.geometry('750x500')
window.title('Time')
window.resizable(False,False)
window['bg']='gray'


def get_wether():
    city = city_name.get()
    r=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = r.json()
    print(data)
    for i,j in data.items():
        print(f'{i}:{j}')

    img = Image.open(f'images/hello.jpg')
    img_tk = ImageTk.PhotoImage(img)

    icon = Label(image=img_tk)
    icon.place(x=230,y=200)

city_name = Entry(fg='orange',font='sanscript 30',bg='gray',width=8)
city_name.place(x=300,y=10)

button_minus = Button(command=get_wether,text='Get weather',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2')
button_minus.place(x=260,y=80)



window.mainloop()