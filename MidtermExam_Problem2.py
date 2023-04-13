from tkinter import *
class Myname:
    def __init__(self,wind):

        self.lbl0 = Label(wind, text="My Full Name")
        self.lbl0.place(x=250,y=50)
        self.lbl1 = Label(wind,text="Enter Given Name:")
        self.lbl1.place(x=150,y=75)
        self.lbl2 = Label(wind,text="Enter Middle Name:")
        self.lbl2.place(x=150,y=105)
        self.lbl3 = Label(wind,text="Enter Last Name:")
        self.lbl3.place(x=150,y=135)
        self.lbl4 = Label(wind,text="My Full Name is:")
        self.lbl4.place(x=150,y=175)
        self.text1 = Entry(wind,bd=2)
        self.text1.place(x=350,y=75)
        self.text2 = Entry(wind,bd=2)
        self.text2.place(x=350,y=105)
        self.text3 = Entry(wind,bd=2)
        self.text3.place(x=350,y=135)
        self.text4 = Entry(wind,bd=2,width=35)
        self.text4.place(x=350,y=175)
        self.btnSFN = Button(wind,text="Show Full Name")
        self.btnSFN.place(x=250,y=210)
        self.btnSFN.bind('<Button-1>',self.sfn)
        self.btnclr = Button(wind,text="Clear")
        self.btnclr.place(x=275,y=240)
        self.btnclr.bind('<Button-1>',self.clr)

    def sfn(self,sfn):
            self.text4.delete(0,'end')
            name1 = str(self.text1.get())
            name2 = str(self.text2.get())
            name3 = str(self.text3.get())
            result = name1 + " " + name2 + " " + name3
            self.text4.insert(END,str(result))

    def clr(self,clr):
            self.text1.delete(0, 'end')
            self.text2.delete(0, 'end')
            self.text3.delete(0, 'end')
            self.text4.delete(0, 'end')


wind = Tk()
mywind = Myname(wind)
wind.geometry("600x400+10+10")
wind.title("MidtermExam_Problem2")
wind.mainloop()