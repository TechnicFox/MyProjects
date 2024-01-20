from tkinter import ttk
from tkinter import *

window = Tk()
window.geometry('600x300')
window.title('Money convector💵')
window.resizable(False,False)
window['bg']='aqua'

label_1_currency = Label(text='1st curency:',fg='blue',font='sanscript 20',bg='aqua')
label_1_currency.place(x=10,y=10)
label_2_currency = Label(text='2st curency:',fg='blue',font='sanscript 20',bg='aqua')
label_2_currency.place(x=350,y=10)

label_enter_ammount = Label(text='Enter ammount:',fg='blue',font='sanscript 20',bg='aqua')
label_enter_ammount.place(x=10,y=100)
label_result = Label(text='Result:',fg='blue',font='sanscript 20',bg='aqua')
label_result.place(x=350,y=100)


box_enter = ttk.Combobox(values=['€','$','£','₴','¥','zł'], background='aqua',foreground='blue',font='sanscript 10',cursor='trek',state='readonly')
box_enter.place(x=10,y=50)
box_enter.set('€')

box_convert = ttk.Combobox(values=['€','$','£','₴','¥','zł'], background='aqua',foreground='blue',font='sanscript 10',cursor='trek',state='readonly')
box_convert.place(x=350,y=50)
box_convert.set('₴')

entry1 = Entry(bg='aqua',font='sanscript 15',fg='blue')
entry1.place(x=10,y=150)
label_result = Label(text='',fg='blue',font='sanscript 15',bg='aqua')
label_result.place(x=350,y=150)

def calculate():
    try:
        if box_enter.get() == '€':
            ans = round(int(entry1.get())*38.56,2)
        elif box_enter.get() == '$':
            ans = round(int(entry1.get())*36.37,2)
        elif box_enter.get() == '£':
            ans = round(int(entry1.get())*44.15,2)
        elif box_enter.get()== '¥':
            ans = round(int(entry1.get())*0.25,2)
        elif box_enter.get()== '₴':
            ans = round(int(entry1.get()),2)
        elif box_enter.get()== 'zł':
            ans = round(int(entry1.get())*8.59,2)

        if box_convert.get()== '€':
            ans = round(ans/38.56,2)
        elif box_convert.get()== '$':
            ans = round(ans/36.37,2)
        elif box_convert.get()== '£':
            ans = round(ans/44.15,2)
        elif box_convert.get() == '¥':
            ans = round(ans/0.25,2)
        elif box_convert.get() == '₴':
            ans = round(ans,2)
        elif box_convert.get() == 'zł':
            ans = round(ans/8.59,2)
        label_result['fg'] = 'blue'
        label_result['text'] = str(ans)
    except:
        label_result['fg'] = 'red'
        label_result['text'] = 'Error 404: Text not allowed'

button = Button(command=calculate,text='💵Convert💵',fg='blue',font='sanscript 40',bg='aqua',activebackground='aqua',activeforeground='blue',borderwidth=0,cursor='cross')
button.pack(side='bottom')

window.mainloop()
