from tkinter import *

root = Tk()

def click():
    p1 = int(e1.get())
    p2 = int(e2.get())

root.title('Test')
root.iconbitmap('images/pcico.ico')

e1 = Entry(root)
e2 = Entry(root)

l1 = Label(root, text='Player1')
l2 = Label(root, text='Player2')
l3 = Label(root, text='Integers (1-10)')

b1 = Button(root, text='Enter', command=click)

l1.grid(row=2, column=1)
l2.grid(row=3, column=1)
l3.grid(row=1, column=1)

e1.grid(row=2, column=2)
e2.grid(row=3, column=2)

b1.grid(row=1, column=3)

root.resizable(False, False)

root.mainloop()