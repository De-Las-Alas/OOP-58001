from tkinter import *
class Mycalc:
    def __init__(self,wind):

#widgets

        self.lbl1 = Label(wind,text="1st No.")
        self.lbl1.place(x=100,y=50)
        self.lbl2 = Label(wind,text="2nd No.")
        self.lbl2.place(x=100,y=100)
        self.lbl3 = Label(wind,text="Result")
        self.lbl3.place(x=100,y=150)
        self.text1 = Entry(wind,bd=1)
        self.text1.place(x=200,y=50)
        self.text2 = Entry(wind,bd=2)
        self.text2.place(x=200,y=100)
        self.text3 = Entry(wind,bd=3)
        self.text3.place(x=200,y=150)
        self.btnadd = Button(wind,text="Addition")
        self.btnadd.place(x=100,y=200)
        self.btnadd.bind('<Button-1>',self.add)
        self.btnsub = Button(wind,text="Subtraction")
        self.btnsub.place(x=160,y=200)
        self.btnsub.bind('<Button-1>',self.sub)
        self.btnmult = Button(wind,text="Multiplication")
        self.btnmult.place(x=235,y=200)
        self.btnmult.bind('<Button-1>',self.mult)
        self.btndiv = Button(wind,text="Division")
        self.btndiv.place(x=324,y=200)
        self.btndiv.bind('<Button-1>',self.div)
        self.btnclr = Button(wind,text="Clear")
        self.btnclr.place(x=380,y=200)
        self.btnclr.bind('<Button-1>',self.clr)

#process/methods

    def add(self,add):
            self.text3.delete(0,'end')
            num1 = float(self.text1.get())
            num2 = float(self.text2.get())
            result = num1 + num2
            self.text3.insert(END,str(result))

    def sub(self,sub):
            self.text3.delete(0,'end')
            num1 = float(self.text1.get())
            num2 = float(self.text2.get())
            result = num1 - num2
            self.text3.insert(END,str(result))

    def mult(self,mult):
            self.text3.delete(0,'end')
            num1 = float(self.text1.get())
            num2 = float(self.text2.get())
            result = num1 * num2
            self.text3.insert(END,str(result))

    def div(self,div):
            self.text3.delete(0,'end')
            num1 = float(self.text1.get())
            num2 = float(self.text2.get())
            result = num1 / num2
            self.text3.insert(END,str(result))

    def clr(self,clr):
            self.text1.delete(0,'end')
            self.text2.delete(0, 'end')
            self.text3.delete(0, 'end')


wind = Tk()
mywind = Mycalc(wind)
wind.geometry("600x400+10+10")
wind.title("Simp. Calc.")
wind.mainloop()
