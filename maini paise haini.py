import tkinter
import tkinter.ttk
import tkinter.messagebox
class form1:
    def add(self):
        if self.textbox1.get()=="" or self.textbox2.get()=="":
            tkinter.messagebox.showinfo("","ALL FIELDS ARE MANDATORY")
        else:
            obj=open("e://group.txt","a")
            grp=self.textbox1.get()
            desc=self.textbox2.get()
            obj.write(grp)
            obj.write("\n")
            obj.write(desc)
            obj.write("\n*************\n")
            obj.close()
            tkinter.messagebox.showinfo("","GROUP ADDED SUCCESSFULLLY")

        
    def __init__(self):
        self.win1=tkinter.Tk()
        self.label1=tkinter.Label(self.win1,text="ENTER GROUP NAME")
        self.textbox1=tkinter.Entry(self.win1)

        self.label2=tkinter.Label(self.win1,text="DESCRIPTION")
        self.textbox2=tkinter.Entry(self.win1)

        self.bt1=tkinter.Button(self.win1,text="SUBMIT",command=self.add)

        self.label1.grid(row=0,column=0)
        self.tex
        tbox1.grid(row=0,column=1)
        self.label2.grid(row=1,column=0)
        self.textbox2.grid(row=1,column=1)
        self.bt1.grid(row=2,column=1)

        self.win1.mainloop()
#-------------------------------------------------------------

def test():
    x=form1()
#-------------------------------------------------------------
def view():
    win2=tkinter.Tk()
    t=tkinter.ttk.Treeview(win2,columns=("grpname","desc"))
    t.heading("grpname",text="GROUP NAME")
    t.heading("desc",text="DESCRIPTION")
    rd=open("e://group.txt","r")
    i=0
    while True:
        grp=rd.readline()
        if grp=="":
            break
        des=rd.readline()
        sep=rd.readline()
        t.insert("",i,values=(grp,des))
        i=i+1
    t.pack()
    win2.mainloop()

#--------------------------------------------------------------

class form3:
    def insert(self):

        wr=open("e:\\numbers.txt","a")
        wr.write(self.cb1.get())
        wr.write(self.textbox2.get())
        wr.write("\n*****\n")
        wr.close()
        tkinter.messagebox.showinfo("","Member Added Sucessfully")
        
    def __init__(self):
        self.win=tkinter.Tk()

        self.lb1=tkinter.Label(self.win,text="Enter Group Name")

        list1=[]

        fileopen=open("e:\\group.txt","r")

        i=0

        while True:
            line=fileopen.readline()
            if line=="":
                break
            line1=fileopen.readline()
            line2=fileopen.readline()
            list1.insert(i,line)
            i=i+1
        fileopen.close()

        print(list1)


        
        self.cb1=tkinter.ttk.Combobox(self.win,values=tuple(list1))


        self.lb2=tkinter.Label(self.win,text="Enter Mobile Number")
        self.textbox2=tkinter.Entry(self.win)

        self.bt1=tkinter.Button(self.win,text="Add New Member",command=self.insert)

        self.lb1.grid(row=0,column=0)
        self.cb1.grid(row=0,column=1)

        self.lb2.grid(row=1,column=0)
        self.textbox2.grid(row=1,column=1)

        self.bt1.grid(row=2,column=1)



        self.win.mainloop()
    


#--------------------------------------------------------------
class form4:
    def insert(self):
        rd=open("e:\\numbers.txt","r")
        i=0
        while True:
            line=rd.readline()
            if line=="":
                break
            line2=rd.readline()
            line3=rd.readline()
            if line==self.cb1.get():
                self.tree.insert("",i,values=((i+1),line,line2))
                i=i+1

        

        
    def __init__(self):
        self.win=tkinter.Tk()
        self.win.geometry("800x800")

        self.frame1=tkinter.Frame(self.win)

        self.lb1=tkinter.Label(self.frame1,text="Enter Group Name")
        self.lb2=tkinter.Label(self.frame1,text="Enter mobile no")
        self.lb3=tkinter.Label(self.frame1,text="Enter message")

        list1=[]

        fileopen=open("e:\\group.txt","r")

        i=0

        while True:
            line=fileopen.readline()
            if line=="":
                break
            line1=fileopen.readline()
            line2=fileopen.readline()
            list1.insert(i,line)
            i=i+1
        fileopen.close()

        print(list1)
        list2=[]

        fileopen=open("e:\\numbers.txt","r")

        i=0

        while True:
            line=fileopen.readline()
            if line=="":
                break
            line1=fileopen.readline()
            line2=fileopen.readline()
            list1.insert(i,line)
            i=i+1
        fileopen.close()

        print(list2)



        
        self.cb1=tkinter.ttk.Combobox(self.frame1,values=tuple(list1))
        self.cb2=tkinter.ttk.Combobox(self.frame1,values=tuple(list2))


       

        self.bt1=tkinter.Button(self.frame1,text="Add New Member",command=self.insert)

        self.lb1.grid(row=0,column=0)
        self.cb1.grid(row=0,column=1)

     

        self.bt1.grid(row=0,column=3)

        self.frame1.pack()

        self.tree=tkinter.ttk.Treeview(self.win,columns=("srno","groupname","members"))
        self.tree.heading("srno",text="Serial Number")
        self.tree.heading("groupname",text="Group Name")
        self.tree.heading("members",text="Mobile Number")
        self.tree.pack()



        self.win.mainloop()

#--------------------------------------------------------------
def showphones():
    x=form4()

#-----------------------

        
def showinsert_data():
    x=form3()

root=tkinter.Tk()
mymenu=tkinter.Menu(root)
root.config(menu=mymenu)
submenu1=tkinter.Menu(mymenu)
submenu1=tkinter.Menu(mymenu,tearoff=False)
mymenu.add_cascade(label="GROUP MANAGEMENT",menu=submenu1)
submenu1.add_command(label="ADD GROUP",command=test)
submenu1.add_command(label="VIEW GROUPS",command=view)
submenu1.add_command(label="Add Contacts",command=showinsert_data)
submenu1.add_command(label="View Contacts",command=showphones)

root.mainloop()
                           




    
