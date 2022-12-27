from tkinter import *
from random import randint

app=Tk()
app.title('Random Generator')
app.geometry('350x100')

def show_msg():
    msg=Label(app,text="Have a nice Day")
    msg.pack()
    
def show_msg1():
    msg=Label(app,text=randint(1,100))
    msg.pack()
    
b= Button(app,text='Click Me',command=show_msg)
b.pack()

b1= Button(app,text='Click',command=show_msg1)
b1.pack()

app.mainloop()