from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
import _datetime
import time

class Customer:

    def __init__(self, root):
        self.root = root
        self.root.title("Customer Billing System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="teal")

        #====================================== VARIABLES =============================================================#
        # system vars
        Date1 = StringVar()
        Time1 = StringVar()
        now = _datetime.datetime.now()
        Date1.set(now.date())
        Time1.set(time.strftime("%H:%M:%S"))

        # user defined vars
        customer_ref = StringVar()
        firstname = StringVar()
        lastname = StringVar()
        address = StringVar()
        pincode = StringVar()
        mobile = StringVar()
        email = StringVar()
        nationality = StringVar()
        dateofbirth = StringVar()
        typeofid = StringVar()
        idproofno = StringVar()
        gender = StringVar()
        invoice_no = StringVar()
        firstpurchase = StringVar()
        lastpurchase = StringVar()

        # tax slabs
        gst5  = 0.05
        gst12 = 0.12
        gst18 = 0.18

        # display vars
        SubTotal = StringVar()
        PaidTax = StringVar()
        Discount = IntVar()
        Total = StringVar()

        # checkboxes
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()

        # Other item description
        E_Other1 = StringVar()
        E_Other2 = StringVar()
        E_Other3 = StringVar()
        E_Other4 = StringVar()
        E_Other5 = StringVar()
        #checkbox item model number
        E_ChairM = StringVar()
        E_TableM = StringVar()
        E_AlmirahM = StringVar()
        E_SofaM = StringVar()
        E_ShowcaseM = StringVar()
        E_CompTableM = StringVar()
        E_WardrobeM = StringVar()
        E_BedM = StringVar()
        E_DiningTableM = StringVar()
        E_Other1M = StringVar()
        E_Other2M = StringVar()
        E_Other3M = StringVar()
        E_Other4M = StringVar()
        E_Other5M = StringVar()
        # checkbox quantity data
        E_Chair = IntVar()
        E_Table = IntVar()
        E_Almirah = IntVar()
        E_Sofa = IntVar()
        E_Showcase = IntVar()
        E_CompTable = IntVar()
        E_Wardrobe = IntVar()
        E_Bed = IntVar()
        E_DiningTable = IntVar()
        E_Other1Q = IntVar()
        E_Other2Q = IntVar()
        E_Other3Q = IntVar()
        E_Other4Q = IntVar()
        E_Other5Q = IntVar()
        # checkbox price
        E_Chair_Price = IntVar()
        E_Table_Price = IntVar()
        E_Almirah_Price = IntVar()
        E_Sofa_Price = IntVar()
        E_Showcase_Price = IntVar()
        E_CompTable_Price = IntVar()
        E_Wardrobe_Price = IntVar()
        E_Bed_Price = IntVar()
        E_DiningTable_Price = IntVar()
        E_Other1_Price = IntVar()
        E_Other2_Price = IntVar()
        E_Other3_Price = IntVar()
        E_Other4_Price = IntVar()
        E_Other5_Price = IntVar()


        #=================================== FUNCTIONS ================================================================#
        def iExit():
            iExit = tkinter.messagebox.askyesno("Customer Billing System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():

            self.txtCus_Ref.delete(0,END)
            self.txtfname.delete(0, END)
            self.txtlname.delete(0, END)
            self.txtaddr.delete(0, END)
            self.txtpcode.delete(0, END)
            self.txtmbl.delete(0, END)
            self.txteml.delete(0, END)
            self.cbonlty.set("")
            self.txtdob.delete(0, END)
            self.cboidtype.set("")
            self.txtidno.delete(0, END)
            self.cbogender.set("")
            self.txtinv_no.delete(0, END)
            self.txtfpdate.delete(0, END)
            self.txtlpdate.delete(0, END)

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)

            E_Chair.set("0")
            E_Table.set("0")
            E_Almirah.set("0")
            E_Sofa.set("0")
            E_Showcase.set("0")
            E_CompTable.set("0")
            E_Wardrobe.set("0")
            E_Bed.set("0")
            E_DiningTable.set("0")

            E_ChairM.set("")
            E_TableM.set("")
            E_AlmirahM.set("")
            E_SofaM.set("")
            E_ShowcaseM.set("")
            E_CompTableM.set("")
            E_WardrobeM.set("")
            E_BedM.set("")
            E_DiningTableM.set("")

            E_Chair_Price.set("0")
            E_Table_Price.set("0")
            E_Almirah_Price.set("0")
            E_Sofa_Price.set("0")
            E_Showcase_Price.set("0")
            E_CompTable_Price.set("0")
            E_Wardrobe_Price.set("0")
            E_Bed_Price.set("0")
            E_DiningTable_Price.set("0")

            E_Other1.set("")
            E_Other2.set("")
            E_Other3.set("")
            E_Other4.set("")
            E_Other5.set("")
            E_Other1M.set("")
            E_Other2M.set("")
            E_Other3M.set("")
            E_Other4M.set("")
            E_Other5M.set("")
            E_Other1Q.set("0")
            E_Other2Q.set("0")
            E_Other3Q.set("0")
            E_Other4Q.set("0")
            E_Other5Q.set("0")
            E_Other1_Price.set("0")
            E_Other2_Price.set("0")
            E_Other3_Price.set("0")
            E_Other4_Price.set("0")
            E_Other5_Price.set("0")


            # self.txtReceipt.delete("1.0", END)

        # Protected checkbox when selected allows editing fields
        def chkChair():
            if (var1.get() == 1):
                self.txtChairM.configure(state=NORMAL)
                self.txtChair.configure(state=NORMAL)
                self.txtChairP.configure(state=NORMAL)
                self.txtChairM.delete(0, END)
                self.txtChair.delete(0, END)
                self.txtChairP.delete(0, END)
                self.txtChairM.focus()
            elif var1.get() == 0:
                self.txtChairM.configure(state=DISABLED)
                self.txtChair.configure(state=DISABLED)
                self.txtChairP.configure(state=DISABLED)
                E_Chair_Price.set("0")

        def chkTable():
            if (var2.get() == 1):
                self.txtTableM.configure(state=NORMAL)
                self.txtTable.configure(state=NORMAL)
                self.txtTableP.configure(state=NORMAL)
                self.txtTableM.delete(0, END)
                self.txtTable.delete(0, END)
                self.txtTableP.delete(0, END)
                self.txtTableM.focus()
            elif var2.get() == 0:
                self.txtTableM.configure(state=DISABLED)
                self.txtTable.configure(state=DISABLED)
                self.txtTableP.configure(state=DISABLED)
                E_Table_Price.set("0")

        def chkAlmirah():
            if (var3.get() == 1):
                self.txtAlmirahM.configure(state=NORMAL)
                self.txtAlmirah.configure(state=NORMAL)
                self.txtAlmirahP.configure(state=NORMAL)
                self.txtAlmirahM.delete(0, END)
                self.txtAlmirah.delete(0, END)
                self.txtAlmirahP.delete(0, END)
                self.txtAlmirahM.focus()
            elif var3.get() == 0:
                self.txtAlmirahM.configure(state=DISABLED)
                self.txtAlmirah.configure(state=DISABLED)
                self.txtAlmirahP.configure(state=DISABLED)
                E_Almirah_Price.set("0")

        def chkSofa():
            if (var4.get() == 1):
                self.txtSofaM.configure(state=NORMAL)
                self.txtSofa.configure(state=NORMAL)
                self.txtSofaP.configure(state=NORMAL)
                self.txtSofaM.delete(0, END)
                self.txtSofa.delete(0, END)
                self.txtSofaP.delete(0, END)
                self.txtSofaM.focus()
            elif var4.get() == 0:
                self.txtSofa.configure(state=DISABLED)
                self.txtSofa.configure(state=DISABLED)
                self.txtSofaP.configure(state=DISABLED)
                E_Sofa_Price.set("0")

        def chkSCase():
            if (var5.get() == 1):
                self.txtSCaseM.configure(state=NORMAL)
                self.txtSCase.configure(state=NORMAL)
                self.txtSCaseP.configure(state=NORMAL)
                self.txtSCaseM.delete(0, END)
                self.txtSCase.delete(0, END)
                self.txtSCaseP.delete(0, END)
                self.txtSCaseM.focus()
            elif var5.get() == 0:
                self.txtSCaseM.configure(state=DISABLED)
                self.txtSCase.configure(state=DISABLED)
                self.txtSCaseP.configure(state=DISABLED)
                E_Sofa_Price.set("0")

        def chkCTable():
            if (var6.get() == 1):
                self.txtCTableM.configure(state=NORMAL)
                self.txtCTable.configure(state=NORMAL)
                self.txtCTableP.configure(state=NORMAL)
                self.txtCTableM.delete(0, END)
                self.txtCTable.delete(0, END)
                self.txtCTableP.delete(0, END)
                self.txtCTableM.focus()
            elif var6.get() == 0:
                self.txtCTableM.configure(state=DISABLED)
                self.txtCTable.configure(state=DISABLED)
                self.txtCTableP.configure(state=DISABLED)
                E_CompTable_Price.set("0")

        def chkWRobe():
            if (var7.get() == 1):
                self.txtWRobeM.configure(state=NORMAL)
                self.txtWRobe.configure(state=NORMAL)
                self.txtWRobeP.configure(state=NORMAL)
                self.txtWRobeM.delete(0, END)
                self.txtWRobe.delete(0, END)
                self.txtWRobeP.delete(0, END)
                self.txtWRobeM.focus()
            elif var7.get() == 0:
                self.txtWRobeM.configure(state=DISABLED)
                self.txtWRobe.configure(state=DISABLED)
                self.txtWRobeP.configure(state=DISABLED)
                E_Wardrobe_Price.set("0")

        def chkBed():
            if (var8.get() == 1):
                self.txtBedM.configure(state=NORMAL)
                self.txtBed.configure(state=NORMAL)
                self.txtBedP.configure(state=NORMAL)
                self.txtBedM.delete(0, END)
                self.txtBed.delete(0, END)
                self.txtBedP.delete(0, END)
                self.txtBedM.focus()
            elif var8.get() == 0:
                self.txtBedM.configure(state=DISABLED)
                self.txtBed.configure(state=DISABLED)
                self.txtBedP.configure(state=DISABLED)
                E_Bed_Price.set("0")

        def chkDTable():
            if (var9.get() == 1):
                self.txtDTableM.configure(state=NORMAL)
                self.txtDTable.configure(state=NORMAL)
                self.txtDTableP.configure(state=NORMAL)
                self.txtDTableM.delete(0, END)
                self.txtDTable.delete(0, END)
                self.txtDTableP.delete(0, END)
                self.txtDTableM.focus()
            elif var9.get() == 0:
                self.txtDTableM.configure(state=DISABLED)
                self.txtDTable.configure(state=DISABLED)
                self.txtDTableP.configure(state=DISABLED)
                E_DiningTable_Price.set("0")

        #====================================== COMPUTATION & DISPLAY =================================================#
        def print_header():
            self.txtReceipt.insert(END, '\t\t TAX INVOICE BILL\t\t\n')
            self.txtReceipt.insert(END, '\t\tSUSHIL FURNITURE\t\t\n')
            self.txtReceipt.insert(END, 'Address:\t4/A Barasat Road, Barrackpore, Kol-120\n')
            self.txtReceipt.insert(END, 'Phone:\t9339152142 | 9123691411\n')
            self.txtReceipt.insert(END, '-'*70 + '\n')

        def print_receipt(sub_total, tax, total):
            spc = "        "
            print_header()
            self.txtReceipt.insert(END, '  Items\t' + 'Model' + '\t' + "Quantity" + spc + "Cost of Items\n")
            self.txtReceipt.insert(END, ("="*40) + "\n")
            if E_Chair.get():
                self.txtReceipt.insert(END, 'Chair:\t' + str(E_ChairM.get()) + '\t' + spc + str(E_Chair.get()) +
                                       "\t\t" + str(E_Chair_Price.get())+"\n")
            if E_Table.get():
                self.txtReceipt.insert(END, 'Table:\t' + str(E_TableM.get()) + '\t' + spc + str(E_Table.get()) +
                                       "\t\t" + str(E_Table_Price.get()) + "\n")
            if E_Almirah.get():
                self.txtReceipt.insert(END, 'Almirah:\t' + str(E_AlmirahM.get()) + '\t' + spc + str(E_Almirah.get()) +
                                       "\t\t" + str(E_Almirah_Price.get()) + "\n")
            if E_Sofa.get():
                self.txtReceipt.insert(END, 'Sofa:\t' + str(E_SofaM.get()) + '\t' + spc + str(E_Sofa.get()) +
                                       "\t\t" + str(E_Sofa_Price.get()) + "\n")
            if E_Showcase.get():
                self.txtReceipt.insert(END, 'Showcase:\t' + str(E_ShowcaseM.get()) + '\t' + spc + str(E_Showcase.get())
                                       + "\t\t" + str(E_Showcase_Price.get()) + "\n")
            if E_CompTable.get():
                self.txtReceipt.insert(END, 'PC Table:\t' + str(E_CompTableM.get()) + '\t' + spc +
                                       str(E_CompTable.get()) + "\t\t" + str(E_CompTable_Price.get()) + "\n")
            if E_Wardrobe.get():
                self.txtReceipt.insert(END, 'Wardrobe:\t' + str(E_WardrobeM.get()) + '\t' + spc + str(E_Wardrobe.get())
                                       + "\t\t" + str(E_Wardrobe_Price.get()) + "\n")
            if E_Wardrobe.get():
                self.txtReceipt.insert(END, 'Bed:\t' + str(E_BedM.get()) + '\t' + spc + str(E_Wardrobe.get()) + "\t\t" +
                                       str(E_Bed_Price.get()) + "\n")
            if E_DiningTable.get():
                self.txtReceipt.insert(END, 'Dining Table:\t' + str(E_DiningTableM.get()) + '\t' + spc +
                                       str(E_DiningTable.get()) + "\t\t" + str(E_DiningTable_Price.get()) + "\n")
            if E_Other1Q.get():
                self.txtReceipt.insert(END, str(E_Other1.get()) + ':\t' + str(E_Other1M.get()) + '\t' + spc +
                                       str(E_Other1Q.get()) + "\t\t" + str(E_Other1_Price.get()) + "\n")
            if E_Other2Q.get():
                self.txtReceipt.insert(END, str(E_Other2.get()) + ':\t' + str(E_Other2M.get()) + '\t' + spc +
                                       str(E_Other2Q.get()) + "\t\t" + str(E_Other2_Price.get()) + "\n")
            if E_Other3Q.get():
                self.txtReceipt.insert(END, str(E_Other3.get()) + ':\t' + str(E_Other3M.get()) + '\t' + spc
                                       + str(E_Other3Q.get()) + "\t\t" + str(E_Other3_Price.get()) + "\n")
            if E_Other4Q.get():
                self.txtReceipt.insert(END, str(E_Other4.get()) + ':\t' + str(E_Other4M.get()) + '\t' + spc
                                       + str(E_Other4Q.get()) + "\t\t" + str(E_Other4_Price.get()) + "\n")
            if E_Other5Q.get():
                self.txtReceipt.insert(END, str(E_Other5.get()) + ':\t' + str(E_Other5M.get()) + '\t' + spc +
                                       str(E_Other5Q.get()) + "\t\t" + str(E_Other5_Price.get()) + "\n")
            self.txtReceipt.insert(END, ("=" * 40) + "\n")
            self.txtReceipt.insert(END, '\nTax Paid:\t\t\t' + tax)
            self.txtReceipt.insert(END, '\nSub Total:\t\t\t' + sub_total + "\n")
            if Discount.get():
                self.txtReceipt.insert(END, 'Discount:\t\t\tRs.' + str(Discount.get()) + '.00\n')
            self.txtReceipt.insert(END, '\nTotal:\t\t\t' + total)
            # print_copy()

        # def print_copy():
        #     print("Inside Copy")
        #     txt = self.txtReceipt.
        #     print(txt)



        def costOfItem():
            customer_ref.set(random.randint(1000, 1000000))
            Item1  = float(E_Chair.get())
            Item1P = float(E_Chair_Price.get())
            Item2 = float(E_Table.get())
            Item2P = float(E_Table_Price.get())
            Item3  = float(E_Almirah.get())
            Item3P = float(E_Almirah_Price.get())
            Item4  = float(E_Sofa.get())
            Item4P = float(E_Sofa_Price.get())
            Item5  = float(E_Showcase.get())
            Item5P = float(E_Showcase_Price.get())
            Item6  = float(E_CompTable.get())
            Item6P = float(E_CompTable_Price.get())
            Item7  = float(E_Wardrobe.get())
            Item7P = float(E_Wardrobe_Price.get())
            Item8  = float(E_Bed.get())
            Item8P = float(E_Bed_Price.get())
            Item9  = float(E_DiningTable.get())
            Item9P = float(E_DiningTable_Price.get())
            Item10  = float(E_Other1Q.get())
            Item10P = float(E_Other1_Price.get())
            Item11  = float(E_Other2Q.get())
            Item11P = float(E_Other2_Price.get())
            Item12  = float(E_Other3Q.get())
            Item12P = float(E_Other3_Price.get())
            Item13  = float(E_Other4Q.get())
            Item13P = float(E_Other4_Price.get())
            Item14  = float(E_Other5Q.get())
            Item14P = float(E_Other5_Price.get())

            price_of_furn = (Item1*Item1P) + (Item2*Item2P) + (Item3*Item3P) + (Item4*Item4P) + (Item5*Item5P) \
                        + (Item6*Item6P) + (Item7*Item7P) + (Item8*Item8P) + (Item9*Item9P) + (Item10*Item10P) \
                        + (Item11*Item11P) + (Item12*Item12P) + (Item13*Item13P) + (Item14*Item14P)
            sub_total_of_items = "Rs.", str('%.2f' %price_of_furn)

            SubTotal.set(sub_total_of_items)
            Tax="Rs.", str('%.2f' %(float(price_of_furn)* gst5)) # 5% GST calculated
            PaidTax.set(Tax)

            if Discount.get():
                TotalAmt = "Rs.", str('%.2f' % ((price_of_furn * (1 + gst5)) - float(Discount.get())))
                Total.set(TotalAmt)
            else:
                TotalAmt = "Rs.", str('%.2f' %(price_of_furn * (1 + gst5)))
                Total.set(TotalAmt)

            sub_total_of_items1 = ''.join(sub_total_of_items)
            tax1 = ''.join(Tax)
            total_amt = ''.join(TotalAmt)

            # Call Print Receipt
            print_receipt(sub_total_of_items1, tax1, total_amt)

        #====================================== SCROLLBAR =============================================================#


        #====================================== FRAMES ================================================================#
        MainFrame = Frame(self.root, bg="teal")
        MainFrame.grid()

        # Define top frame
        DataFrameTop = Frame(MainFrame, bd=14, width=1350, height=100, padx=10, relief=RIDGE, bg="teal")
        DataFrameTop.grid(row=0, column=0, columnspan=4, sticky=W)

        # Define Left Frame
        DataFrameLeft = Frame(MainFrame, bd=14, width=450, height=488, padx=10, relief=RIDGE, bg="teal")
        DataFrameLeft.grid(row=1, column=0, sticky=W)
        # Define Left Cust Detail Frame
        DataFrameLeftTop = Frame(DataFrameLeft, bd=14, width=450, height=488, padx=10, relief=RIDGE, bg="teal")
        DataFrameLeftTop.grid(row=0, column=0, sticky=W)
        # Define Left Button Frame
        DataFrameLeftBut = Frame(DataFrameLeft, bd=14, width=370, height=80, padx=10, relief=RIDGE, bg="powder blue")
        DataFrameLeftBut.grid(row=1, column=0, sticky=W)

        # Define Middle Frame
        DataFrameMid = Frame(MainFrame, bd=14, width=450, height=488, padx=2, relief=RIDGE, bg="powder blue")
        DataFrameMid.grid(row=1, column=1, sticky=W)

        # Define Right Frames(top and bottom)
        DataFrameRight = Frame(MainFrame, bd=14, width=450, height=488, padx=10, relief=RIDGE, bg="teal")
        DataFrameRight.grid(row=1, column=2, sticky=W)
        # Right Top
        DataFrameRightTop = Frame(DataFrameRight, bd=14, width=370, height=340, padx=10, relief=RIDGE, bg="powder blue")
        DataFrameRightTop.grid(row=0, column=0, sticky=W)
        # Right Bottom
        DataFrameRightBot = Frame(DataFrameRight, bd=14, width=370, height=120, padx=10, relief=RIDGE, bg="teal")
        DataFrameRightBot.grid(row=1, column=0, sticky=W)
        # Right Bottom Buttons
        DataFrameRightBut = Frame(DataFrameRight, bd=14, width=370, height=80, padx=10, relief=RIDGE, bg="powder blue")
        DataFrameRightBut.grid(row=2, column=0, sticky=W)

        #====================================== LABELS & ENTRY WIDGETS ================================================#
        # title label and headers
        self.lbltitl = Label(DataFrameTop, font=('arial', 32, 'bold'), bg="powder blue", fg="#0a243c",
                             text="\tCustomer Billing Software\t\t", bd=5, pady=9).grid(row=0, column=1)
        self.lbltitl = Label(DataFrameTop, font=('arial', 24, 'bold'), bg="powder blue", fg="purple",
                             textvariable=Date1, bd=5, pady=9).grid(row=0, column=0)
        self.lbltitl = Label(DataFrameTop, font=('arial', 24, 'bold'), bg="powder blue", fg="purple",
                             textvariable=Time1, bd=5, pady=9).grid(row=0, column=2)

        # Customer Details labels and entry
        self.lblCus_Ref = Label(DataFrameLeftTop, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                                text="Customer Ref:")
        self.lblCus_Ref.grid(row=0, column=0, sticky=W)
        self.txtCus_Ref = Entry(DataFrameLeftTop, font=('arial', 12, 'bold'), width=20, textvariable=customer_ref)
        self.txtCus_Ref.grid(row=0, column=1, pady=3,padx=20)

        self.lblfname = Label(DataFrameLeftTop, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                                text="Firstname:")
        self.lblfname.grid(row=1, column=0, sticky=W)
        self.txtfname = Entry(DataFrameLeftTop, font=('arial', 12, 'bold'), width=20, textvariable=firstname)
        self.txtfname.grid(row=1, column=1, pady=3, padx=20)

        self.lbllname = Label(DataFrameLeftTop, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                                text="Surname:")
        self.lbllname.grid(row=2, column=0, sticky=W)
        self.txtlname = Entry(DataFrameLeftTop, font=('arial', 12, 'bold'), width=20, textvariable=lastname)
        self.txtlname.grid(row=2, column=1, pady=3, padx=20)

        self.lbladdr = Label(DataFrameLeftTop, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                                text="Address:")
        self.lbladdr.grid(row=3, column=0, sticky=W)
        self.txtaddr = Entry(DataFrameLeftTop, font=('arial', 12, 'bold'), width=20, textvariable=address)
        self.txtaddr.grid(row=3, column=1, pady=3, padx=20)

        self.lblpcode = Label(DataFrameLeftTop, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                                text="Pincode:")
        self.lblpcode.grid(row=4, column=0, sticky=W)
        self.txtpcode = Entry(DataFrameLeftTop, font=('arial', 12, 'bold'), width=20, textvariable=pincode)
        self.txtpcode.grid(row=4, column=1, pady=3, padx=20)

        self.lblmbl = Label(DataFrameLeftTop, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                                text="Mobile:")
        self.lblmbl.grid(row=5, column=0, sticky=W)
        self.txtmbl = Entry(DataFrameLeftTop, font=('arial', 12, 'bold'), width=20, textvariable=mobile)
        self.txtmbl.grid(row=5, column=1, pady=3, padx=20)

        self.lbleml = Label(DataFrameLeftTop, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                                text="Email:")
        self.lbleml.grid(row=6, column=0, sticky=W)
        self.txteml = Entry(DataFrameLeftTop, font=('arial', 12, 'bold'), width=20, textvariable=email)
        self.txteml.grid(row=6, column=1, pady=3, padx=20)

        self.lblnlty = Label(DataFrameLeftTop, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                                text="Nationality:")
        self.lblnlty.grid(row=7, column=0, sticky=W)
        self.cbonlty = ttk.Combobox(DataFrameLeftTop, font=('arial', 12, 'bold'), width=18, textvariable=nationality, state='readonly')
        self.cbonlty['value'] = ['','India','Bangladesh','Nepal','Bhutan','Others']
        self.cbonlty.current(1)
        self.cbonlty.grid(row=7, column=1, pady=3, padx=20)

        self.lbldob = Label(DataFrameLeftTop, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                                text="D.O.B :")
        self.lbldob.grid(row=8, column=0, sticky=W)
        self.txtdob = Entry(DataFrameLeftTop, font=('arial', 12, 'bold'), width=20, textvariable=dateofbirth)
        self.txtdob.grid(row=8, column=1, pady=3, padx=20)

        self.lblidtype = Label(DataFrameLeftTop, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                                text="Type of ID:")
        self.lblidtype.grid(row=9, column=0, sticky=W)
        self.cboidtype = ttk.Combobox(DataFrameLeftTop, font=('arial', 12, 'bold'), width=18, textvariable=typeofid, state='readonly')
        self.cboidtype['value'] = ('', 'Voter ID', 'Adhar Card', 'PAN Card', 'Driving License', 'Passport', 'Others')
        self.cboidtype.current(0)
        self.cboidtype.grid(row=9, column=1, pady=3, padx=20)

        self.lblidno = Label(DataFrameLeftTop, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                            text="ID Number :")
        self.lblidno.grid(row=10, column=0, sticky=W)
        self.txtidno = Entry(DataFrameLeftTop, font=('arial', 12, 'bold'), width=20, textvariable=idproofno)
        self.txtidno.grid(row=10, column=1, pady=3, padx=20)

        self.lblgender = Label(DataFrameLeftTop, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                                text="Gender:")
        self.lblgender.grid(row=11, column=0, sticky=W)
        self.cbogender = ttk.Combobox(DataFrameLeftTop, font=('arial', 12, 'bold'), width=18, textvariable=gender, state='readonly')
        self.cbogender['value'] = ('', 'Male', 'Female')
        self.cbogender.current(0)
        self.cbogender.grid(row=11, column=1, pady=3, padx=20)

        self.lblinv_no = Label(DataFrameLeftTop, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                                text="Invoice No:")
        self.lblinv_no.grid(row=12, column=0, sticky=W)
        self.txtinv_no = Entry(DataFrameLeftTop, font=('arial', 12, 'bold'), width=20, textvariable=invoice_no)
        self.txtinv_no.grid(row=12, column=1, pady=3, padx=20)

        self.lblfpdate = Label(DataFrameLeftTop, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                                text="First Pur Date:")
        self.lblfpdate.grid(row=13, column=0, sticky=W)
        self.txtfpdate = Entry(DataFrameLeftTop, font=('arial', 12, 'bold'), width=20, textvariable=firstpurchase)
        self.txtfpdate.grid(row=13, column=1, pady=3, padx=20)

        self.lbllpdate = Label(DataFrameLeftTop, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                                text="Last Pur Date:")
        self.lbllpdate.grid(row=14, column=0, sticky=W)
        self.txtlpdate = Entry(DataFrameLeftTop, font=('arial', 12, 'bold'), width=20, textvariable=lastpurchase)
        self.txtlpdate.grid(row=14, column=1, pady=3, padx=20)

        self.txtReceipt = Text(DataFrameRightTop, height=19, width=43, bd=10, font=('arial', 9, 'bold'))
        self.txtReceipt.grid(row=0,column=0)

        #================================= CheckButton & ENTRY WIDGETS ================================================#
        self.lblprod = Label(DataFrameMid, font=('arial', 14, 'bold'), bg="powder blue", fg="#0a243c",
                             text="Product", bd=5, pady=9)
        self.lblprod.grid(row=0, column=0)
        self.lblprod = Label(DataFrameMid, font=('arial', 14, 'bold'), bg="powder blue", fg="#0a243c",
                             text="Model", bd=5, pady=9)
        self.lblprod.grid(row=0, column=1)
        self.lblprod = Label(DataFrameMid, font=('arial', 14, 'bold'), bg="powder blue", fg="#0a243c",
                             text="Quantity", bd=5, pady=9)
        self.lblprod.grid(row=0, column=2)
        self.lblprod = Label(DataFrameMid, font=('arial', 14, 'bold'), bg="powder blue", fg="#0a243c",
                             text="Price", bd=5, pady=9)
        self.lblprod.grid(row=0, column=3)

        self.Chair = Checkbutton(DataFrameMid, text="Chair", variable=var1, onvalue=1, offvalue=0, command=chkChair,
                                 font=('arial', 12, 'bold'), bg="powder blue")
        self.Chair.grid(row=1,sticky=W)
        self.txtChairM = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=20, justify=LEFT, state=DISABLED,
                              textvariable=E_ChairM)
        self.txtChairM.grid(row=1, column=1)
        self.txtChair = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                              textvariable=E_Chair)
        self.txtChair.grid(row=1,column=2)
        self.txtChairP = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=RIGHT, state=DISABLED,
                              textvariable=E_Chair_Price)
        self.txtChairP.grid(row=1,column=3)

        self.Table = Checkbutton(DataFrameMid, text="Table", variable=var2, onvalue=1, offvalue=0, command=chkTable,
                                 font=('arial', 12, 'bold'), bg="powder blue")
        self.Table.grid(row=2, sticky=W)
        self.txtTableM = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=20, justify=LEFT, state=DISABLED,
                              textvariable=E_TableM)
        self.txtTableM.grid(row=2, column=1)
        self.txtTable = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                              textvariable=E_Table)
        self.txtTable.grid(row=2, column=2)
        self.txtTableP = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=RIGHT, state=DISABLED,
                              textvariable=E_Table_Price)
        self.txtTableP.grid(row=2, column=3)

        self.Almirah = Checkbutton(DataFrameMid, text="Almirah", variable=var3, onvalue=1, offvalue=0, command=chkAlmirah,
                                 font=('arial', 12, 'bold'), bg="powder blue")
        self.Almirah.grid(row=3, sticky=W)
        self.txtAlmirahM = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=20, justify=LEFT, state=DISABLED,
                                textvariable=E_AlmirahM)
        self.txtAlmirahM.grid(row=3, column=1)
        self.txtAlmirah = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                              textvariable=E_Almirah)
        self.txtAlmirah.grid(row=3, column=2)
        self.txtAlmirahP = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=RIGHT, state=DISABLED,
                              textvariable=E_Almirah_Price)
        self.txtAlmirahP.grid(row=3, column=3)

        self.Sofa = Checkbutton(DataFrameMid, text="Sofa", variable=var4, onvalue=1, offvalue=0, command=chkSofa,
                                 font=('arial', 12, 'bold'), bg="powder blue")
        self.Sofa.grid(row=4, sticky=W)
        self.txtSofaM = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=20, justify=LEFT, state=DISABLED,
                             textvariable=E_SofaM)
        self.txtSofaM.grid(row=4, column=1)
        self.txtSofa = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                              textvariable=E_Sofa)
        self.txtSofa.grid(row=4, column=2)
        self.txtSofaP = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=RIGHT, state=DISABLED,
                              textvariable=E_Sofa_Price)
        self.txtSofaP.grid(row=4, column=3)

        self.SCase = Checkbutton(DataFrameMid, text="Showcase", variable=var5, onvalue=1, offvalue=0, command=chkSCase,
                                 font=('arial', 12, 'bold'), bg="powder blue")
        self.SCase.grid(row=5, sticky=W)
        self.txtSCaseM = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=20, justify=LEFT, state=DISABLED,
                              textvariable=E_ShowcaseM)
        self.txtSCaseM.grid(row=5, column=1)
        self.txtSCase = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                              textvariable=E_Showcase)
        self.txtSCase.grid(row=5, column=2)
        self.txtSCaseP = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=RIGHT, state=DISABLED,
                              textvariable=E_Showcase_Price)
        self.txtSCaseP.grid(row=5, column=3)

        self.CTable = Checkbutton(DataFrameMid, text="Comp Table", variable=var6, onvalue=1, offvalue=0, command=chkCTable,
                                 font=('arial', 12, 'bold'), bg="powder blue")
        self.CTable.grid(row=6, sticky=W)
        self.txtCTableM = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=20, justify=LEFT, state=DISABLED,
                               textvariable=E_CompTableM)
        self.txtCTableM.grid(row=6, column=1)
        self.txtCTable = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                              textvariable=E_CompTable)
        self.txtCTable.grid(row=6, column=2)
        self.txtCTableP = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=RIGHT, state=DISABLED,
                              textvariable=E_CompTable_Price)
        self.txtCTableP.grid(row=6, column=3)

        self.WRobe = Checkbutton(DataFrameMid, text="Wardrobe", variable=var7, onvalue=1, offvalue=0, command=chkWRobe,
                                 font=('arial', 12, 'bold'), bg="powder blue")
        self.WRobe.grid(row=7, sticky=W)
        self.txtWRobeM = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=20, justify=LEFT, state=DISABLED,
                              textvariable=E_WardrobeM)
        self.txtWRobeM.grid(row=7, column=1)
        self.txtWRobe = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                              textvariable=E_Wardrobe)
        self.txtWRobe.grid(row=7, column=2)
        self.txtWRobeP = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=RIGHT, state=DISABLED,
                              textvariable=E_Wardrobe_Price)
        self.txtWRobeP.grid(row=7, column=3)

        self.Bed = Checkbutton(DataFrameMid, text="Bed", variable=var8, onvalue=1, offvalue=0, command=chkBed,
                                 font=('arial', 12, 'bold'), bg="powder blue")
        self.Bed.grid(row=8, sticky=W)
        self.txtBedM = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=20, justify=LEFT, state=DISABLED,
                            textvariable=E_BedM)
        self.txtBedM.grid(row=8, column=1)
        self.txtBed = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                              textvariable=E_Bed)
        self.txtBed.grid(row=8, column=2)
        self.txtBedP = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=RIGHT, state=DISABLED,
                              textvariable=E_Bed_Price)
        self.txtBedP.grid(row=8, column=3)

        self.DTable = Checkbutton(DataFrameMid, text="Dining Table", variable=var9, onvalue=1, offvalue=0, command=chkDTable,
                                 font=('arial', 12, 'bold'), bg="powder blue")
        self.DTable.grid(row=9, sticky=W)
        self.txtDTableM = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=20, justify=LEFT, state=DISABLED,
                               textvariable=E_DiningTableM)
        self.txtDTableM.grid(row=9, column=1)
        self.txtDTable = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                              textvariable=E_DiningTable)
        self.txtDTable.grid(row=9, column=2)
        self.txtDTableP = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=RIGHT, state=DISABLED,
                              textvariable=E_DiningTable_Price)
        self.txtDTableP.grid(row=9, column=3)

        self.Other1 = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=LEFT,
                            textvariable=E_Other1)
        self.Other1.grid(row=10, column=0)
        self.Other1M = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=20, justify=LEFT,
                             textvariable=E_Other1M)
        self.Other1M.grid(row=10, column=1)
        self.Other1Q = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=6, justify=LEFT,
                            textvariable=E_Other1Q)
        self.Other1Q.grid(row=10, column=2)
        self.Other1P = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=RIGHT,
                            textvariable=E_Other1_Price)
        self.Other1P.grid(row=10, column=3)

        self.Other2 = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=LEFT,
                            textvariable=E_Other2)
        self.Other2.grid(row=11, column=0)
        self.Other2M = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=20, justify=LEFT,
                             textvariable=E_Other2M)
        self.Other2M.grid(row=11, column=1)
        self.Other2Q = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=6, justify=LEFT,
                             textvariable=E_Other2Q)
        self.Other2Q.grid(row=11, column=2)
        self.Other2P = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=RIGHT,
                             textvariable=E_Other2_Price)
        self.Other2P.grid(row=11, column=3)

        self.Other3 = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=LEFT,
                            textvariable=E_Other3)
        self.Other3.grid(row=12, column=0)
        self.Other3M = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=20, justify=LEFT,
                             textvariable=E_Other3M)
        self.Other3M.grid(row=12, column=1)
        self.Other3Q = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=6, justify=LEFT,
                             textvariable=E_Other3Q)
        self.Other3Q.grid(row=12, column=2)
        self.Other3P = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=RIGHT,
                             textvariable=E_Other3_Price)
        self.Other3P.grid(row=12, column=3)

        self.Other4 = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=LEFT,
                            textvariable=E_Other4)
        self.Other4.grid(row=13, column=0)
        self.Other4M = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=20, justify=LEFT,
                             textvariable=E_Other4M)
        self.Other4M.grid(row=13, column=1)
        self.Other4Q = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=6, justify=LEFT,
                             textvariable=E_Other4Q)
        self.Other4Q.grid(row=13, column=2)
        self.Other4P = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=RIGHT,
                             textvariable=E_Other4_Price)
        self.Other4P.grid(row=13, column=3)

        self.Other5 = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=LEFT,
                            textvariable=E_Other5)
        self.Other5.grid(row=14, column=0)
        self.Other5M = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=20, justify=LEFT,
                             textvariable=E_Other5M)
        self.Other5M.grid(row=14, column=1)
        self.Other5Q = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=6, justify=LEFT,
                             textvariable=E_Other5Q)
        self.Other5Q.grid(row=14, column=2)
        self.Other5P = Entry(DataFrameMid, font=('arial', 12, 'bold'), bd=8, width=10, justify=RIGHT,
                             textvariable=E_Other5_Price)
        self.Other5P.grid(row=14, column=3)

        # Right Middle Totals Labels and Entry
        self.lblSTotal = Label(DataFrameRightBot, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                               text="Sub Total")
        self.lblSTotal.grid(row=0, column=0, sticky=W)
        self.txtSTotal = Entry(DataFrameRightBot, font=('arial', 12, 'bold'), width=20, textvariable=SubTotal)
        self.txtSTotal.grid(row=0, column=1, pady=3, padx=20)
        self.lblTax = Label(DataFrameRightBot, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                              text="Tax")
        self.lblTax.grid(row=1, column=0, sticky=W)
        self.txtTax = Entry(DataFrameRightBot, font=('arial', 12, 'bold'), width=20, textvariable=PaidTax)
        self.txtTax.grid(row=1, column=1, pady=3, padx=20)
        self.lblDisc = Label(DataFrameRightBot, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                            text="Discount")
        self.lblDisc.grid(row=2, column=0, sticky=W)
        self.txtDisc = Entry(DataFrameRightBot, font=('arial', 12, 'bold'), width=20, textvariable=Discount)
        self.txtDisc.grid(row=2, column=1, pady=3, padx=20)
        self.lblTotal = Label(DataFrameRightBot, font=('arial', 12, 'bold'), padx=2, bg="teal", fg="Cornsilk",
                              text="Total")
        self.lblTotal.grid(row=3, column=0, sticky=W)
        self.txtTotal = Entry(DataFrameRightBot, font=('arial', 12, 'bold'), width=20, textvariable=Total)
        self.txtTotal.grid(row=3, column=1, pady=3, padx=20)




        #====================================== BUTTONS ===============================================================#
        # Right Buttons
        self.BtnTotal = Button(DataFrameRightBut, padx=8, pady=4, font=('arial', 16, 'bold'), bg="powder blue", fg="black",
                          width=4, height=2, text="Total", relief=RIDGE, command=costOfItem).grid(row=0, column=0)
        self.BtnReset = Button(DataFrameRightBut, padx=8, pady=4, font=('arial', 16, 'bold'), bg="powder blue", fg="black",
                               width=4, height=2, text="Print", relief=RIDGE).grid(row=0, column=1)
        self.BtnReset = Button(DataFrameRightBut, padx=8, pady=4, font=('arial', 16, 'bold'), bg="powder blue", fg="black",
                          width=4, height=2, text="Reset", relief=RIDGE, command=clearData).grid(row=0, column=2)
        self.BtnExit = Button(DataFrameRightBut, padx=8, pady=4, font=('arial', 16, 'bold'), bg="powder blue", fg="black",
                          width=4, height=2, text="Exit", relief=RIDGE, command=iExit).grid(row=0, column=3)
        # Left Buttons
        self.BtnInv = Button(DataFrameLeftBut, padx=8, pady=4, font=('arial', 16, 'bold'), bg="powder blue", fg="black",
                               width=10, height=2, text="Inventory", relief=RIDGE).grid(row=0, column=0)
        self.BtnCDetl = Button(DataFrameLeftBut, padx=8, pady=4, font=('arial', 16, 'bold'), bg="powder blue", fg="black",
                               width=10, height=2, text="Cust Details", relief=RIDGE).grid(row=0, column=1)



#=================================== MAIN FUNCTION ====================================================================#
if __name__ == '__main__':
    root = Tk()
    app = Customer(root)
    root.mainloop()