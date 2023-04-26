from tkinter import *
window = Tk()
window.geometry("500x400+10+10")
window.title("Ambotsaimo")

btm1 = Button(window, text="Don't Click Me", fg="white", bg="black")
btm1.pack(side = "top")
btm1.place(x=225, y=200)
txtfld = Entry(window, border=2.40)
txtfld.place(x=100, y=140)
lbl = Label(window, text = "1st Demo", font = "Verdana")
lbl.place(x=15, y=25)
window.mainloop()
