import tkinter
import tkinter.messagebox
#---------------------------------------------------------------------------
class form1:
    def add(self):
        while True:
            if self.textbox1=="":
                self.tkinter.messagebox.showinfo("","** Fields are mandatory")
                break
                
            else:
                obj=open("E:\\New folder\\group_record.txt","a")
                Group_Name=self.textbox1.get()
                Description=self.textbox2.get()
                obj.write(Group_Name)
                obj.write("\n")
                obj.write(Description)
                obj.write("\n")
                obj.write("*******\n")
                obj.close()
                tkinter.messagebox.showinfo("","Group Created Succesfully")
                break
    def __init__(self):
        self.root=tkinter.Tk()
        self.lb1=tkinter.Label(self.root,text="Create a new group")
        self.lb2=tkinter.Label(self.root,text="Group Name**")
        self.textbox1=tkinter.Entry(self.root)
        self.lb3=tkinter.Label(self.root,text="description")
        self.textbox2=tkinter.Entry(self.root)
        self.bt1=tkinter.Button(self.root,text="Submit",command=self.add)
        #this is the grid code
        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=1,column=0)
        self.textbox1.grid(row=1,column=1)
        self.lb3.grid(row=2,column=0)
        self.textbox2.grid(row=2,column=1)
        self.bt1.grid(row=3,column=1)
        self.root.mainloop()
#=====================================================================

x=form1()
        
        
    




















