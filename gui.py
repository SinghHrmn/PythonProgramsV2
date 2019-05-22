import tkinter
import tkinter.messagebox
#------------------------------------------------------------------------------
def test():
    tkinter.messagebox.showinfo("","hello world")
def test2():
    tkinter.messagebox.showinfo("","bye world")
def test3():
    tkinter.messagebox.showinfo("","im learning python")
#------------------------------------------------------------------------------
    
root=tkinter.Tk()
mymenu=tkinter.Menu(root)
root.config(menu=mymenu)
submenu1=tkinter.Menu(mymenu)
mymenu.add_cascade(label="file",menu=submenu1)
submenu1.add_command(label="new file",command=test)
submenu1.add_command(label="open file",command=test2)
submenu1.add_separator()
submenu1.add_command(label="open file ",command=test3)





root.mainloop()
