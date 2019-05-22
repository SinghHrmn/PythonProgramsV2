import tkinter
import tkinter.ttk
import tkinter.messagebox


# ------------------------------------------------------------------------
class Form1:
    def add(self):
        if self.textbox1.get() == "":
            tkinter.messagebox.showinfo("", "** Fields are mandatory")

        else:

            obj = open("E:\\python vmm\\group_record.txt", "a")
            group_name = self.textbox1.get()
            description = self.textbox2.get()
            obj.write(group_name)
            obj.write("\n")
            obj.write(description)
            obj.write("\n")
            obj.write("*******\n")
            obj.close()
            tkinter.messagebox.showinfo("", "Group Created Successfully")

    def __init__(self):
        self.root = tkinter.Tk()
        self.lb1 = tkinter.Label(self.root, text="Create a new group")
        self.lb2 = tkinter.Label(self.root, text="Group Name**")
        self.textbox1 = tkinter.Entry(self.root)
        self.lb3 = tkinter.Label(self.root, text="description")
        self.textbox2 = tkinter.Entry(self.root)
        self.bt1 = tkinter.Button(self.root, text="Submit", command=self.add)
        # this is the grid code
        self.lb1.grid(row=0, column=0)
        self.lb2.grid(row=1, column=0)
        self.textbox1.grid(row=1, column=1)
        self.lb3.grid(row=2, column=0)
        self.textbox2.grid(row=2, column=1)
        self.bt1.grid(row=3, column=1)
        self.root.mainloop()


# ---------------------------------------------------------------------------------------------------
def showresult():
    root = tkinter.Tk()
    t = tkinter.ttk.Treeview(root, columns=("Group_Name", "Description"))
    t.heading("Group_Name", text="Group Name")
    t.heading("Description", text="Description")
    rd = open("E:\python vmm\\group_record.txt", "r")
    i = 0
    while True:
        Group_Name = rd.readline()
        if Group_Name == "":
            break
        description = rd.readline()
        seperator = rd.readline()
        t.insert("", i, values=(Group_Name, description))
        i = i + 1
    t.pack()


# -------------------------------------------------------------------------------------------------------
root = tkinter.Tk()
mymenu = tkinter.Menu(root)
root.config(menu=mymenu)
submenu1 = tkinter.Menu(mymenu, tearoff=0)
mymenu.add_cascade(label="File", menu=submenu1)
submenu1.add_command(label="Create Group", command=form1)
submenu1.add_command(label="View list of Groups", command=showresult)
root.mainloop()
