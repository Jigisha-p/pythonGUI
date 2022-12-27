from tkinter import *
from random import choice

app=Tk()
app.title('Element picker')
app.geometry('350x100')

inp=Entry(app)
inp.pack()

def pick():
    INP=(inp.get()).split(',')
    msg=Label(app,text=choice(INP))
    msg.pack()
    
b= Button(app,text='Choose',command=pick)
b.pack()


app.mainloop()