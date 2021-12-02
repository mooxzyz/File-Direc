from tkinter import *
import os

root = Tk()

root.geometry('250x65')

root.title('School Com')

myEntry = Entry(root, border=2)

def ostom():
	os.system(str(myEntry.get()))
	myEntry.delete(0, END)

myButton = Button(root, text="click here", command=ostom, border=2)

myButton.pack()
myEntry.pack()
root.resizable(False, False)
root.iconbitmap('./pcico.ico')

root.mainloop()