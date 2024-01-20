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


    img = Image.open(f'images/{data['weather'][0]['icon']}.png')
    img2 = img.resize([300,300])
    img_tk = ImageTk.PhotoImage(img2)

    icon = Label(image=img_tk,bg='gray')
    icon.image = img_tk
    icon.place(x=220,y=160)

    img_arrow = Image.open(f'images/arrow.png')
    img2_arrow = img_arrow.resize([125,125]).rotate(data['wind']['deg'])
    img_tk_arrow = ImageTk.PhotoImage(img2_arrow)

    icon = Label(image=img_tk_arrow,bg='gray')
    icon.image = img_tk_arrow
    icon.place(x=550,y=370)

    city_wind = Label(text=f'Wind\n{data['wind']['speed']}m/s',fg='orange',bg='gray',font='sanscript 30',width=7,height=3)
    city_wind.place(x=530,y=245)

    city_temp = Label(text=f'Temp\n{data['main']['temp']}°C',fg='orange',bg='gray',font='sanscript 30',width=7,height=3)
    city_temp.place(x=50,y=50)

    city_humidity = Label(text=f'Humidity\n{data['main']['humidity']}%',fg='orange',bg='gray',font='sanscript 30')
    city_humidity.place(x=50,y=250)

    city_pressure = Label(text=f'Pressure\n{data['main']['pressure']}hPa',fg='orange',bg='gray',font='sanscript 30')
    city_pressure.place(x=550,y=65)

    city_country = Label(text=f'{data['sys']['country']}',fg='orange',bg='gray',font='sanscript 30')
    city_country.place(x=345,y=420)

    city_country['text']=f'{data['sys']['country']}'
    city_humidity['text']=f'Humidity\n{data['main']['humidity']}%'
    city_temp['text']=f'Temp\n{data['main']['temp']}°C'
    

city_name = Entry(fg='orange',font='sanscript 30',bg='gray',width=8)
city_name.place(x=300,y=10)



button_minus = Button(command=get_wether,text='Get weather',font='sanscript 30',bg='gray',fg='orange',activeforeground='orange',activebackground='gray',cursor='hand2')
button_minus.place(x=260,y=80)



window.mainloop()