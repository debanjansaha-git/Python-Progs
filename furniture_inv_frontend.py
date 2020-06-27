# Frontend SourceCode for Furniture Inventory
from tkinter import *
import tkinter.messagebox
import furniture_inv_backend

class Furniture:

    def __init__(self, root):
        self.root = root
        self.root.title = "Sushil Furniture Inventory"
        self.root.geometry("1350x7500+0+0")
        self.root.config(bg="teal")

        # Defining Variables
        Manufacturer = StringVar()
        Item_Name = StringVar()
        Price = StringVar()
        Color = StringVar()
        Dimension = StringVar()
        Weight = StringVar()
        Item_Model_No = StringVar()
        Quantity = StringVar()
        Assemby_Req = StringVar()
        Pri_Material = StringVar()
        Capacity = StringVar()
        Warranty = StringVar()

        #================================ FUNCTIONS ===================================================================#

        def iExit():
            iExit = tkinter.messagebox.askyesno("Sushil Furniture Inventory","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtmanu.delete(0, END)
            self.txtitemnm.delete(0, END)
            self.txtprice.delete(0, END)
            self.txtcolor.delete(0, END)
            self.txtdimm.delete(0, END)
            self.txtwght.delete(0, END)
            self.txtitmmdl.delete(0, END)
            self.txtqty.delete(0, END)
            self.txtasmrq.delete(0, END)
            self.txtpmat.delete(0, END)
            self.txtcap.delete(0, END)
            self.txtwarr.delete(0, END)

        def addData():
            if (len(Item_Name.get()) != 0):
                furniture_inv_backend.addNewItem(Manufacturer.get(), Item_Name.get(), Price.get(), Color.get(),
                                                 Dimension.get(), Weight.get(), Item_Model_No.get(), Quantity.get(),
                                                 Assemby_Req.get(), Pri_Material.get(), Capacity.get(), Warranty.get())
                furniturelist.delete(0, END)
                furniturelist.insert(END, (Manufacturer.get(), Item_Name.get(), Price.get(), Color.get(),
                                                Dimension.get(), Weight.get(), Item_Model_No.get(), Quantity.get(),
                                                Assemby_Req.get(), Pri_Material.get(), Capacity.get(), Warranty.get()))

        def displayData():
            furniturelist.delete(0, END)
            for row in furniture_inv_backend.viewData():
                furniturelist.insert(END,row,str(""))

        def furnitureRec(event):
            global fd
            searchFurn = furniturelist.curselection()[0]
            fd = furniturelist.get(searchFurn)
            self.txtmanu.delete(0, END)
            self.txtmanu.insert(END, fd[1])
            self.txtitemnm.delete(0, END)
            self.txtitemnm.insert(END, fd[2])
            self.txtprice.delete(0, END)
            self.txtprice.insert(END, fd[3])
            self.txtcolor.delete(0, END)
            self.txtcolor.insert(END, fd[4])
            self.txtdimm.delete(0, END)
            self.txtdimm.insert(END, fd[5])
            self.txtwght.delete(0, END)
            self.txtwght.insert(END, fd[6])
            self.txtitmmdl.delete(0, END)
            self.txtitmmdl.insert(END, fd[7])
            self.txtqty.delete(0, END)
            self.txtqty.insert(END, fd[8])
            self.txtasmrq.delete(0, END)
            self.txtasmrq.insert(END, fd[9])
            self.txtpmat.delete(0, END)
            self.txtpmat.insert(END, fd[10])
            self.txtcap.delete(0, END)
            self.txtcap.insert(END, fd[11])
            self.txtwarr.delete(0, END)
            self.txtwarr.insert(END, fd[12])

        def deleteData():
            if (len(Item_Name.get()) != 0):
                furniture_inv_backend.deleteRec(fd[0])
                clearData()
                displayData()

        def searchDatabase():
            furniturelist.delete(0, END)
            for row in furniture_inv_backend.searchData(Manufacturer.get(), Item_Name.get(), Price.get(), Color.get(),
                                                 Dimension.get(), Weight.get(), Item_Model_No.get(), Quantity.get(), Assemby_Req.get(),
                                                 Pri_Material.get(), Capacity.get(), Warranty.get()):
                furniturelist.insert(END,row,str(""))

        def update():
            if (len(Item_Name.get()) != 0):
                furniture_inv_backend.deleteRec(fd[0])
            if (len(Item_Name.get()) != 0):
                furniture_inv_backend.addNewItem(Manufacturer.get(), Item_Name.get(), Price.get(), Color.get(),
                                                 Dimension.get(), Weight.get(), Item_Model_No.get(), Quantity.get(), Assemby_Req.get(),
                                                 Pri_Material.get(), Capacity.get(), Warranty.get())
                furniturelist.delete(0, END)
                furniturelist.insert(END, (Manufacturer.get(), Item_Name.get(), Price.get(), Color.get(),
                                                 Dimension.get(), Weight.get(), Item_Model_No.get(), Quantity.get(), Assemby_Req.get(),
                                                 Pri_Material.get(), Capacity.get(), Warranty.get()))




        #================================== FRAMES ====================================================================#

        MainFrame = Frame(self.root, bg="teal")
        MainFrame.grid()

        # Defining Title Frame at the Top
        TitlFrame = Frame(MainFrame, bd=2, padx=10, pady=10, bg="Ghost White", relief=RIDGE)
        TitlFrame.pack(side=TOP)

        # Defining Button Frame at the Bottom
        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=10, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        # Defining Data Frame in the middle
        DataFrame = Frame(MainFrame, bd=2, width=1300, height=700, padx=10, pady=10, bg="teal", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)
        # Left Frame Labels
        DataFrameLeft = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=10, bg="Ghost White", relief=RIDGE,
                              font=('arial', 20, 'bold'), text="Product Information\n")
        DataFrameLeft.pack(side=LEFT)
        # Right Frame Labels
        DataFrameRight = LabelFrame(DataFrame, bd=1, width=400, height=700, padx=10, bg="Ghost White", relief=RIDGE,
                               font=('arial', 20, 'bold'), text="Product Details\n")
        DataFrameRight.pack(side=RIGHT)

        #================================== LABELS & ENTRY WIDGETS ====================================================#

        self.lbltitle = Label(TitlFrame, font=('arial', 32, 'bold'), bg="Ghost White",
                              text="Sushil Furniture Inventory")
        self.lbltitle.grid()
        # Left Dataframe Labels & Entry
        self.lblmanu = Label(DataFrameLeft, font=('arial', 16, 'bold'), bg="Ghost White", padx=2, pady=2,
                             text="Manufacturer")
        self.lblmanu.grid(row=0, column=0, sticky=W)
        self.txtmanu = Entry(DataFrameLeft, font=('arial', 16), bg="Ghost White", width=40,
                             textvariable=Manufacturer)
        self.txtmanu.grid(row=0, column=1)

        self.lblitemnm = Label(DataFrameLeft, font=('arial', 16, 'bold'), bg="Ghost White", padx=2, pady=2,
                             text="Item Name")
        self.lblitemnm.grid(row=1, column=0, sticky=W)
        self.txtitemnm = Entry(DataFrameLeft, font=('arial', 16), bg="Ghost White", width=40,
                             textvariable=Item_Name)
        self.txtitemnm.grid(row=1, column=1)

        self.lblprice = Label(DataFrameLeft, font=('arial', 16, 'bold'), bg="Ghost White", padx=2, pady=2,
                             text="Price")
        self.lblprice.grid(row=2, column=0, sticky=W)
        self.txtprice = Entry(DataFrameLeft, font=('arial', 16), bg="Ghost White", width=40,
                             textvariable=Price)
        self.txtprice.grid(row=2, column=1)

        self.lblcolor = Label(DataFrameLeft, font=('arial', 16, 'bold'), bg="Ghost White", padx=2, pady=2,
                             text="Color")
        self.lblcolor.grid(row=3, column=0, sticky=W)
        self.txtcolor = Entry(DataFrameLeft, font=('arial', 16), bg="Ghost White", width=40,
                             textvariable=Color)
        self.txtcolor.grid(row=3, column=1)

        self.lbldimm = Label(DataFrameLeft, font=('arial', 16, 'bold'), bg="Ghost White", padx=2, pady=2,
                             text="Dimension")
        self.lbldimm.grid(row=4, column=0, sticky=W)
        self.txtdimm = Entry(DataFrameLeft, font=('arial', 16), bg="Ghost White", width=40,
                             textvariable=Dimension)
        self.txtdimm.grid(row=4, column=1)

        self.lblwght = Label(DataFrameLeft, font=('arial', 16, 'bold'), bg="Ghost White", padx=2, pady=2,
                             text="Weight")
        self.lblwght.grid(row=5, column=0, sticky=W)
        self.txtwght = Entry(DataFrameLeft, font=('arial', 16), bg="Ghost White", width=40,
                             textvariable=Weight)
        self.txtwght.grid(row=5, column=1)

        self.lblitmmdl = Label(DataFrameLeft, font=('arial', 16, 'bold'), bg="Ghost White", padx=2, pady=2,
                             text="Item Model No")
        self.lblitmmdl.grid(row=6, column=0, sticky=W)
        self.txtitmmdl = Entry(DataFrameLeft, font=('arial', 16), bg="Ghost White", width=40,
                             textvariable=Item_Model_No)
        self.txtitmmdl.grid(row=6, column=1)

        self.lblqty = Label(DataFrameLeft, font=('arial', 16, 'bold'), bg="Ghost White", padx=2, pady=2,
                              text="Quantity")
        self.lblqty.grid(row=7, column=0, sticky=W)
        self.txtqty = Entry(DataFrameLeft, font=('arial', 16), bg="Ghost White", width=40,
                              textvariable=Quantity)
        self.txtqty.grid(row=7, column=1)

        self.lblasmrq = Label(DataFrameLeft, font=('arial', 16, 'bold'), bg="Ghost White", padx=2, pady=2,
                             text="Assemby Required")
        self.lblasmrq.grid(row=8, column=0, sticky=W)
        self.txtasmrq = Entry(DataFrameLeft, font=('arial', 16), bg="Ghost White", width=40,
                             textvariable=Assemby_Req)
        self.txtasmrq.grid(row=8, column=1)

        self.lblpmat = Label(DataFrameLeft, font=('arial', 16, 'bold'), bg="Ghost White", padx=2, pady=2,
                             text="Primary Material")
        self.lblpmat.grid(row=9, column=0, sticky=W)
        self.txtpmat = Entry(DataFrameLeft, font=('arial', 16), bg="Ghost White", width=40,
                             textvariable=Pri_Material)
        self.txtpmat.grid(row=9, column=1)

        self.lblcap = Label(DataFrameLeft, font=('arial', 16, 'bold'), bg="Ghost White", padx=2, pady=2,
                             text="Capacity")
        self.lblcap.grid(row=10, column=0, sticky=W)
        self.txtcap = Entry(DataFrameLeft, font=('arial', 16), bg="Ghost White", width=40,
                             textvariable=Capacity)
        self.txtcap.grid(row=10, column=1)

        self.lblwarr = Label(DataFrameLeft, font=('arial', 16, 'bold'), bg="Ghost White", padx=2, pady=2,
                             text="Warranty")
        self.lblwarr.grid(row=11, column=0, sticky=W)
        self.txtwarr = Entry(DataFrameLeft, font=('arial', 16), bg="Ghost White", width=40,
                             textvariable=Warranty)
        self.txtwarr.grid(row=11, column=1)

        #================================== LISTBOX & SCROLLBAR WIDGETS ===============================================#

        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky='ns')
        furniturelist = Listbox(DataFrameRight, height=16, width=20, font=('arial', 12),
                                yscrollcommand=scrollbar.set)
        furniturelist.bind('<<ListboxSelect>>', furnitureRec)
        furniturelist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=furniturelist.yview)

        #======================================= BUTTON WIDGETS =======================================================#

        self.btnAddNew = Button(ButtonFrame, text="Add New", width=10, height=1, bd=4,
                                font=('arial', 20, 'bold'), command=addData)
        self.btnAddNew.grid(row=0, column=0)

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
    root.title("Inventory")
    app = Furniture(root)
    root.mainloop()