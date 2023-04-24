from tkinter import *
win = Tk()
win.geometry("400x200+10+10")
win.title("Grid Manager")

#widgets

txt1 = Entry(win, bd=2, justify="center")
txt1.grid(row=0,column=0)
txt1.insert(0, "row 0" + " " + " " "column 0")

txt2 = Entry(win, bd=2, justify="center")
txt2.grid(row=0,column=1)
txt2.insert(0, "row 0" + " " + " " "column 1")

txt2 = Entry(win, bd=2, justify="center")
txt2.grid(row=0,column=2)
txt2.insert(0, "row 0" + " " + " " "column 2")

txt2 = Entry(win, bd=2, justify="center")
txt2.grid(row=1,column=0)
txt2.insert(1, "row 1" + " " + " " "column 0")

txt2 = Entry(win, bd=2, justify="center")
txt2.grid(row=1,column=1)
txt2.insert(1, "row 1" + " " + " " "column 1")

txt2 = Entry(win, bd=2, justify="center")
txt2.grid(row=1,column=2)
txt2.insert(1, "row 1" + " " + " " "column 2")

txt2 = Entry(win, bd=2, justify="center")
txt2.grid(row=2,column=0)
txt2.insert(2, "row 2" + " " + " " "column 0")

txt2 = Entry(win, bd=2, justify="center")
txt2.grid(row=2,column=1)
txt2.insert(2, "row 2" + " " + " " "column 1")

txt2 = Entry(win, bd=2, justify="center")
txt2.grid(row=2,column=2)
txt2.insert(2, "row 2" + " " + " " "column 2")

txt2 = Entry(win, bd=2, justify="center")
txt2.grid(row=3,column=0)
txt2.insert(3, "row 3" + " " + " " "column 0")

txt2 = Entry(win, bd=2, justify="center")
txt2.grid(row=3,column=1)
txt2.insert(3, "row 3" + " " + " " "column 1")

txt2 = Entry(win, bd=2, justify="center")
txt2.grid(row=3,column=2)
txt2.insert(3, "row 3" + " " + " " "column 2")

win.mainloop()
