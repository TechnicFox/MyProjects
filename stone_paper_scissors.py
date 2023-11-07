from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('600x600')
window.title('✂️🪨📃')
window.resizable(False,False)
window['bg']='gray'

label_computer_choice_text = Label(text='Computer choice:',fg='white',font='sanscript 20',bg='gray')
label_computer_choice_text.place(x=210,y=10)


label_computer_choice = Label(text='❓',fg='white',font='sanscript 100',bg='gray')
label_computer_choice.place(x=230,y=50)


def stone():
    pass
def scissors():
    label_computer_choice['text']='✂️'
def paper():
    pass


button_stone = Button(command=stone,text='🪨',font='sanscript 100',bg='gray',fg='darkgray',activeforeground='darkgray',activebackground='gray',borderwidth=0,cursor='hand2')
button_stone.place(x=-35,y=375)
button_scissors = Button(command=scissors,text='✂️',font='sanscript 100',bg='gray',activebackground='gray',borderwidth=0,cursor='hand2')
button_scissors.place(x=175,y=375)
button_paper = Button(command=paper,text='📃',fg='white',activeforeground='white',font='sanscript 100',bg='gray',activebackground='gray',borderwidth=0,cursor='hand2')
button_paper.place(x=400,y=375)



window.mainloop()
