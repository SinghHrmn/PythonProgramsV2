import tkinter
import tkinter.messagebox
#---------------------------------------------------------------
class form1:
    def demo(self):
        tkinter.messagebox.showinfo("","im learning multipledocuments")
    def __init__(self):
        self.win=tkinter.Tk()
        self.lb=tkinter.Label(self.win,text="Enter String")
        self.textbox1=tkinter.Entry(self.win)
        self.bt1=tkinter.Button(self.win,text="Press",command=self.demo)
        self.lb.grid(row=0,column=0)
        self.textbox1(row=0,column=1)
        self.bt1.grid(row=1,column=1)
        self.win.mainloop()
#---------------------------------------------------------------
def test():
    tkinter.messagebox.showinfo("","hello world")
def test2():
    tkinter.messagebox.showinfo("","bye world")
def test3():
    tkinter.messagebox.showinfo("","im learning python")
#------------------------------------------------------------------------------
root=tkinter.Tk()
root.geometry("600x600")
mymenu=tkinter.Menu(root)
root.config(menu=mymenu)
submenu1=tkinter.Menu(mymenu)
mymenu.add_cascade(label="file",menu=submenu1)
submenu1.add_command(label="new file",command=form1)
submenu1.add_command(label="open file",command=test2)
submenu1.add_separator()
submenu1.add_command(label="open file ",command=test3)
root.mainloop()


