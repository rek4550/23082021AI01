import tkinter as tkr
app=tkr.Tk(__name__)
app.title('My Calculator')
app.geometry('400x400')
tkr.Label(app, text='Enter first number').place(x=15, y=15)
tkr.Label(app, text='Enter second number').place(x=250, y=10)
tkr.Label(app, text='Result').place(x=100, y=50)
v1=tkr.Variable(app)
v2=tkr.Variable(app)
t=tkr.Variable(app)
tkr.Entry(app, textvariable=v1).place(x=15, y=30)
tkr.Entry(app, textvariable=v2).place(x=250, y=50)
tkr.Entry(app, textvariable=t).place(x=70, y=70)


def func1():
    print(int(v1.get())+int(v2.get()))
    t.set(int(v1.get())+int(v2.get()))

def func2():
    print(int(v1.get())-int(v2.get()))
    t.set(int(v1.get())-int(v2.get()))

def func3():
    print(int(v1.get())/int(v2.get()))
    t.set(int(v1.get())/int(v2.get()))

def func4():
    print(int(v1.get())*int(v2.get()))
    t.set(int(v1.get())*int(v2.get()))

tkr.Button(app, text='+',command=func1,bg='red').place(x=150,y=100)
tkr.Button(app, text='-',command=func2,bg='red').place(x=190,y=100)
tkr.Button(app, text='/',command=func3,bg='red').place(x=210,y=100)
tkr.Button(app, text='*',command=func4,bg='red').place(x=250,y=100)

app.mainloop()
