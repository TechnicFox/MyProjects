from tkinter import *
import sys
from tkinter import messagebox

import upsidedown



username_info= 'admin'
password_info = '12345678'


window = Tk()
window.geometry('600x300')
window.title('Login and Sign Up')
window.resizable(False,False)
window['bg']='aqua'

label_username = Label(text='Username:',fg='blue',font='sanscript 20',bg='aqua')
label_username.pack()
label_password = Label(text='Password:',fg='blue',font='sanscript 20',bg='aqua')
label_password.place(x=235,y=100)

entry_username = Entry(bg='aqua',font='sanscript 15',fg='blue')
entry_username.place(x=190,y=50)
entry_password = Entry(bg='aqua',font='sanscript 15',fg='blue',show='*')
entry_password.place(x=190,y=150)

def log_in():
    if entry_username.get()==username_info and entry_password.get()==password_info:
        messagebox.showinfo("Login INFO","Username:✅, Password:✅") 
    elif entry_username.get()!=username_info and entry_password.get()!=password_info:
        messagebox.showerror("Login INFO","Username:❌, Password:❌") 
    elif entry_username.get()!=username_info and entry_password.get()==password_info:
        messagebox.showerror("Login INFO","Username:❌, Password:✅") 
    elif entry_username.get()==username_info and entry_password.get()!=password_info:
        messagebox.showerror("Login INFO","Username:✅, Password:❌") 
def help():
    messagebox.showinfo("Hint",upsidedown.transform(f'password:{password_info}\nusername:{username_info}')) 
def exit_app():
    sys.exit()

login_words = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_"
password_no_words = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ+=;:”“‘’/|, "

def login_check(login,log_words,flag=False):
    for i in login:
        if i in log_words:
            flag =True
    if flag:
        return True
    else:
        return False
def password_check(password,password_words,flag=True,max=8):
    if len(password)>=max:
        for i in password:
            if i in password_words:
                flag=False
    else:
        flag=False
    if flag:
        return True
    else:
        return False
def sign_up():
    global username_info
    global password_info
    username = entry_username.get()
    password = entry_password.get()
    if login_check(username,login_words) and password_check(password,password_no_words):
        if username_info==username and password_info==password:
            messagebox.showerror("INFO","Account is already created")
        else:
            messagebox.showinfo("INFO","Username:✅, Password:✅")
            username_info=username
            password_info=password
    elif login_check(username,login_words) == False and password_check(password,password_no_words) == False:
        messagebox.showerror("INFO","Username:❌, Password:❌") 
    elif login_check(username,login_words) == False and password_check(password,password_no_words):
        messagebox.showerror("INFO","Username:❌, Password:✅") 
    elif login_check(username,login_words) and password_check(password,password_no_words) == False:
        messagebox.showerror("INFO","Username:✅, Password:❌") 

button_Login = Button(command=log_in,text='Log in',fg='Green',font='sanscript 25',bg='aqua',activebackground='aqua',activeforeground='green',borderwidth=0,cursor='cross')
button_Login.place(x=260,y=205)
button_Login = Button(command=sign_up,text='Sign up',fg='Green',font='sanscript 25',bg='aqua',activebackground='aqua',activeforeground='green',borderwidth=0,cursor='cross')
button_Login.place(x=130,y=205)
button_help = Button(command=help,text='?',fg='Green',font='sanscript 30',bg='aqua',activebackground='aqua',activeforeground='green',borderwidth=0,cursor='cross')
button_help.place(x=360,y=200)
button_exit = Button(command=exit_app,text='❌',fg='red',font='sanscript 30',bg='aqua',activebackground='aqua',activeforeground='green',borderwidth=0,cursor='cross')
button_exit.place(x=395,y=200)

window.mainloop()
