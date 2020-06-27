# FrontEnd

from tkinter import *
import tkinter.messagebox
import stdDatabase_backend

class Student:

    def __init__(self, root):
        self.root = root
        self.root.title = "Student Database Management System"
        self.root.geometry("1350x7500+0+0")
        self.root.config(bg="cadet blue")

        # Defining all variables
        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Dob = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        # ==============================Functions======================================#

        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Database Management System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtStuID.delete(0,END)
            self.txtfname.delete(0, END)
            self.txtlname.delete(0, END)
            self.txtdob.delete(0, END)
            self.txtage.delete(0, END)
            self.txtgender.delete(0, END)
            self.txtaddr.delete(0, END)
            self.txtmobl.delete(0, END)

        def addData():
            if(len(StdID.get()) !=0):
                stdDatabase_backend.addStdRec(StdID.get(), Firstname.get(), Surname.get(), Dob.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Surname.get(), Dob.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))

        def displayData():
            studentlist.delete(0, END)
            for row in stdDatabase_backend.viewData():
                studentlist.insert(END,row,str(""))

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)
            self.txtStuID.delete(0, END)
            self.txtStuID.insert(END,sd[1])
            self.txtfname.delete(0, END)
            self.txtfname.insert(END, sd[2])
            self.txtlname.delete(0, END)
            self.txtlname.insert(END, sd[3])
            self.txtdob.delete(0, END)
            self.txtdob.insert(END, sd[4])
            self.txtage.delete(0, END)
            self.txtage.insert(END, sd[5])
            self.txtgender.delete(0, END)
            self.txtgender.insert(END, sd[6])
            self.txtaddr.delete(0, END)
            self.txtaddr.insert(END, sd[7])
            self.txtmobl.delete(0, END)
            self.txtmobl.insert(END, sd[8])

        def deleteData():
            if (len(StdID.get()) != 0):
                stdDatabase_backend.deleteRec(sd[0])
                clearData()
                displayData()

        def searchDatabase():
            studentlist.delete(0,END)
            for row in stdDatabase_backend.searchData(StdID.get(), Firstname.get(), Surname.get(), Dob.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()):
                studentlist.insert(END,row,str(""))

        def update():
            if (len(StdID.get()) !=0):
                stdDatabase_backend.deleteRec(sd[0])
            if (len(StdID.get()) !=0):
                stdDatabase_backend.addStdRec(StdID.get(), Firstname.get(), Surname.get(), Dob.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Surname.get(), Dob.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))

        #==============================Frames========================================================#
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitlFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        TitlFrame.pack(side=TOP)

        self.lbltitl = Label(TitlFrame, font=('arial', 47, 'bold'), bg="Ghost White",
                             text="Student Database Management System")
        self.lbltitl.grid()
        self.lbltitl.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, bg="cadet blue", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, width=1000, height=600, bd=1, padx=20, bg="Ghost White", relief=RIDGE,
                                   font=('arial', 20, 'bold'), text="Student Information\n")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, width=450, height=300, bd=1, padx=31, pady=3, bg="Ghost White", relief=RIDGE,
                                    font=('arial', 20, 'bold'), text="Student Details\n")
        DataFrameRight.pack(side=RIGHT)

        #==============================Labels and Entry Widget======================================#
        self.lblStuID = Label(DataFrameLeft, font=('arial', 20, 'bold'), padx=2, pady=2, bg="Ghost White",
                             text="Student ID")
        self.lblStuID.grid(row=0, column=0, sticky=W)
        self.txtStuID = Entry(DataFrameLeft, font=('arial', 20, 'bold'), width=39,
                              textvariable=StdID)
        self.txtStuID.grid(row=0, column=1)

        self.lblfname = Label(DataFrameLeft, font=('arial', 20, 'bold'), padx=2, pady=2, bg="Ghost White",
                              text="FirstName")
        self.lblfname.grid(row=1, column=0, sticky=W)
        self.txtfname = Entry(DataFrameLeft, font=('arial', 20, 'bold'), width=39,
                              textvariable=Firstname)
        self.txtfname.grid(row=1, column=1)

        self.lbllname = Label(DataFrameLeft, font=('arial', 20, 'bold'), padx=2, pady=2, bg="Ghost White",
                              text="Surname")
        self.lbllname.grid(row=2, column=0, sticky=W)
        self.txtlname = Entry(DataFrameLeft, font=('arial', 20, 'bold'), width=39,
                              textvariable=Surname)
        self.txtlname.grid(row=2, column=1)

        self.lbldob = Label(DataFrameLeft, font=('arial', 20, 'bold'), padx=2, pady=2, bg="Ghost White",
                              text="Date of Birth")
        self.lbldob.grid(row=3, column=0, sticky=W)
        self.txtdob = Entry(DataFrameLeft, font=('arial', 20, 'bold'), wi   dth=39,
                              textvariable=Dob)
        self.txtdob.grid(row=3, column=1)

        self.lblage = Label(DataFrameLeft, font=('arial', 20, 'bold'), padx=2, pady=2, bg="Ghost White",
                              text="Age")
        self.lblage.grid(row=4, column=0, sticky=W)
        self.txtage = Entry(DataFrameLeft, font=('arial', 20, 'bold'), width=39,
                              textvariable=Age)
        self.txtage.grid(row=4, column=1)

        self.lblgender = Label(DataFrameLeft, font=('arial', 20, 'bold'), padx=2, pady=2, bg="Ghost White",
                              text="Gender")
        self.lblgender.grid(row=5, column=0, sticky=W)
        self.txtgender = Entry(DataFrameLeft, font=('arial', 20, 'bold'), width=39,
                              textvariable=Gender)
        self.txtgender.grid(row=5, column=1)

        self.lbladdr = Label(DataFrameLeft, font=('arial', 20, 'bold'), padx=2, pady=2, bg="Ghost White",
                              text="Address")
        self.lbladdr.grid(row=6, column=0, sticky=W)
        self.txtaddr = Entry(DataFrameLeft, font=('arial', 20, 'bold'), width=39,
                              textvariable=Address)
        self.txtaddr.grid(row=6, column=1)

        self.lblmobl = Label(DataFrameLeft, font=('arial', 20, 'bold'), padx=2, pady=2, bg="Ghost White",
                              text="Mobile")
        self.lblmobl.grid(row=7, column=0, sticky=W)
        self.txtmobl = Entry(DataFrameLeft, font=('arial', 20, 'bold'), width=39,
                              textvariable=Mobile)
        self.txtmobl.grid(row=7, column=1)
        # ==============================ListBox & ScrollBar Widget=========================#

        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = Listbox(DataFrameRight, width=41, height=16, font=('arial', 12, 'bold'),
                              yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command = studentlist.yview)


        # ==============================Button Widget======================================#

        self.btnAddDate = Button(ButtonFrame, text="Add New", width=10, height=1, bd=4,
                                 font=('arial', 20, 'bold'), command=addData)
        self.btnAddDate.grid(row=0, column=0)

        self.btnDisplay = Button(ButtonFrame, text="Display", width=10, height=1, bd=4,
                                 font=('arial', 20, 'bold'), command=displayData)
        self.btnDisplay.grid(row=0, column=1)

        self.btnClear = Button(ButtonFrame, text="Clear", width=10, height=1, bd=4,
                                 font=('arial', 20, 'bold'), command=clearData)
        self.btnClear.grid(row=0, column=2)

        self.btnDelete = Button(ButtonFrame, text="Delete", width=10, height=1, bd=4,
                                 font=('arial', 20, 'bold'), command=deleteData)
        self.btnDelete.grid(row=0, column=3)

        self.btnSearch = Button(ButtonFrame, text="Search", width=10, height=1, bd=4,
                                 font=('arial', 20, 'bold'), command=searchDatabase)
        self.btnSearch.grid(row=0, column=4)

        self.btnUpdate = Button(ButtonFrame, text="Update", width=10, height=1, bd=4,
                                 font=('arial', 20, 'bold'), command=update)
        self.btnUpdate.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", width=10, height=1, bd=4,
                                 font=('arial', 20, 'bold'), command=iExit)
        self.btnExit.grid(row=0, column=6)


if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()