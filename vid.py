from tkinter import *
import os
from tkinter.font import Font

root = Tk()

comic = Font(
    family="Comic Sans MS",
    size=20,
)

root.iconbitmap('./pcico.ico')

root.title('Vid')

root.geometry('394x400')

def idk():
    os.system('shutdown /p')

bg = PhotoImage(file='./images/flushed.gif')

label = Label(root, image=bg)
label.place(x=0, y=0, relwidth=1, relheight=1)


button_one = Button(root, text='Click Here', command=idk, padx=50, pady=50, font=comic)

button_one.pack()

root.resizable(False, False)

root.mainloop()

