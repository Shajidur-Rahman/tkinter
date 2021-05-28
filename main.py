#########################################
# reset all
from tkinter import *
root = Tk() 


########################################
# creating a tkinter 

# from tkinter import *
# root = Tk()
# my_lable = Label(root, text='Hello World')
# my_lable.pack()
# root.mainloop()


############################################
#positioning 

# my_lable = Label(root, text='Hello world ')
# my_lable2 = Label(root, text='My name is shajidur rahman')

# my_lable.grid(row=0, column=0)
# my_lable2.grid(row=1, column=0)

# root.mainloop()


###############################################
#creating buttons

def myclick():
    mylable = Label(root, text='I click the button', fg='blue', bg='red')
    mylable.pack()

mybottons = Button(root, text='Click fme', padx=30, pady=30) # padx and pady to resize 
# mybottons = Button(root, text='Click me', command=myclick, fg='blue', bg='black') # command for running a function 
# fg for item color and bg for background color
mybottons.pack()

root.mainloop()