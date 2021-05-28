from tkinter import *
root = Tk() 

e = Entry(root)
e.pack()
get = e.get()

def myclick():
    mylable = Label(root, text=e.get())
    mylable.pack()
mybutton = Button(root, text='Click me', command=myclick)
mybutton.pack()

def myexit():
    exit()
myexitb = Button(root, text='Exit', command=myexit)
myexitb.pack()

root.mainloop()