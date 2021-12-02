from tkinter import *
import os

root = Tk()

def shutdown():
    os.system('shutdown /p')

myButton = Button(root, text="Shutdown", padx=50, pady=50, command=shutdown)

myButton.pack()

root.iconbitmap('./pcico.ico')

root.mainloop()
