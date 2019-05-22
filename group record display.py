import tkinter
import tkinter.ttk
#------------------------------------------------------------------
root=tkinter.Tk()
t=tkinter.ttk.Treeview(root,columns=("Group_Name","Description"))
t.heading("Group_Name",text="Group Name")
t.heading("Description",text="Description")
rd=open("E:\\New folder\\group_record.txt","r")
i=0
while True:
    Group_Name=rd.readline()
    if Group_Name=="":
        break
    description=rd.readline()
    seperator=rd.readline()
    t.insert("",i,values=(Group_Name,description))
    i=i+1
t.pack()














root.mainloop()
