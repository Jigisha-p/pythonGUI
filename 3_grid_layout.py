from tkinter import *
from random import choice

app=Tk()
app.title('Element picker')
app.geometry('350x100')

inp=Entry(app)
inp.grid(row=0, column=0, columnspan=2, padx=25, pady=5)


def pick():
    INP=(inp.get()).split(',')
    ch="Choice="+str(choice(INP))
    msg=Label(app,text=ch)
    msg.grid(row=2, column=0, columnspan=2, padx=25, pady=5)
    
b1= Button(app,text='Choose',command=pick)
b1.grid(row=1, column=0, padx=25, pady=5)

b2= Button(app,text='Cancel',command=app.quit)
b2.grid(row=1, column=1, padx=25, pady=5)

app.mainloop()