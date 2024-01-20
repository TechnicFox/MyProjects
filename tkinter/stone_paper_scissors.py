from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.geometry('600x600')
window.title('✂️🪨📃')
window.resizable(False,False)
window['bg']='gray'

label_computer_choice_text = Label(text='Computer choice:',fg='white',font='sanscript 20',bg='gray')
label_computer_choice_text.place(x=210,y=10)


label_computer_choice = Label(text='❓',fg='white',font='sanscript 100',bg='gray')
label_computer_choice.place(x=230,y=50)

def pc_choice(number):
    choices = [['🪨','darkgray'],['📃','white'],['✂️','black']]
    pc_choice_type = random.choice(choices)
    label_computer_choice['text']=pc_choice_type[0]
    label_computer_choice['fg']=pc_choice_type[1]
    if (number == 1 and pc_choice_type[0]=='🪨') or (number == 2 and pc_choice_type[0]=='📃') or (number == 3 and pc_choice_type[0]=='✂️'):
        messagebox.showinfo("✂️🪨📃","Draw😓")
    elif (number == 1 and pc_choice_type[0]=='📃') or (number == 2 and pc_choice_type[0]=='✂️') or (number == 3 and pc_choice_type[0]=='🪨'):
        messagebox.showinfo("✂️🪨📃","You LOSE😓")
    elif (number == 1 and pc_choice_type[0]=='✂️') or (number == 2 and pc_choice_type[0]=='🪨') or (number ==3 and pc_choice_type[0]=='📃'):
        messagebox.showinfo("✂️🪨📃","You WON🎉")

button_stone = Button(command=lambda:pc_choice(1),text='🪨',font='sanscript 100',bg='gray',fg='darkgray',activeforeground='darkgray',activebackground='gray',borderwidth=0,cursor='hand2')
button_stone.place(x=-35,y=375)
button_paper = Button(command=lambda:pc_choice(2),text='📃',fg='white',activeforeground='white',font='sanscript 100',bg='gray',activebackground='gray',borderwidth=0,cursor='hand2')
button_paper.place(x=400,y=375)
button_scissors = Button(command=lambda:pc_choice(3),text='✂️',font='sanscript 100',bg='gray',activebackground='gray',borderwidth=0,cursor='hand2')
button_scissors.place(x=175,y=375)




window.mainloop()
