# def show_balance():
#
#
# def credit_acc(amt, bal):
#
#
# def debit_acc(amt, bal):

def new_entry():
    # defining Tkinter variables
    input_txt = StringVar()
    input_amt = StringVar()
    notes_txt = StringVar()
    date_dd = IntVar()
    date_mm = IntVar()
    date_yyyy = IntVar()
#    combo_acc = Combobox(window)

    # create a frame for display of balance
    disp_frame = Frame(window, height=20, width = 500, bg='yellow')
    disp_frame.pack(side=TOP)

    # create 2nd frame for input of items
    inp_frame = Frame(window, height=200, width=500)
    inp_frame.pack(side=TOP)
    bot_frame = Frame(window, height=150, width=500)
    bot_frame.pack(side=BOTTOM)

    # creating fields inside input frame
    # combo_acc['type'] = ("Savings", "Current", "Recurring")
    # combo_acc.current(0)
    # combo_acc.grid(row=0, column=1)
    l1 = Label(inp_frame, text="Account Type", font=('arial', 9), justify=LEFT)
    l1.grid(row=0, column=0, ipady=2)

    l2 = Label(inp_frame, text="Description", font=('arial', 9), justify=LEFT)
    l2.grid(row=1, column=0, ipady=2)
    inp_field1 = Entry(inp_frame, font=('arial', 9), textvariable=input_txt, justify=CENTER)
    inp_field1.grid(row=1, column=1, ipady=2)

    l3 = Label(inp_frame, text="Amount", font=('arial', 9), justify=LEFT)
    l3.grid(row=2, column=0, ipady=2)
    inp_field2 = Entry(inp_frame, font=('arial', 9), textvariable=input_amt, justify=RIGHT)
    inp_field2.grid(row=2, column=1, ipady=2)

    # creating radio buttons for credit or debit
    l4 = Label(inp_frame, text="Type")
    r1 = Radiobutton(inp_frame, text="Debit", value=1)
    r2 = Radiobutton(inp_frame, text="Credit", value=2)
    l4.grid(row=3, column=0, ipadx=2)
    r1.grid(row=3, column=1, ipadx=2)
    r2.grid(row=3, column=2, ipadx=2)

    l5 = Label(inp_frame, text="Date")
    l5.grid(row=4, column=0, ipadx=2)
    date_dd_field = Entry(inp_frame, textvariable=date_dd, width=5, justify=RIGHT)
    date_dd_field.grid()
    l6 = Label(inp_frame, text="Time")
    l6.grid(row=4, column=1, ipadx=2)

    l7 = Label(inp_frame, text="Category")
    l7.grid(row=5, column=0, ipady=2)

    l8 = Label(inp_frame, text="Notes")
    l8.grid(row=6, column=0, ipady=2)
    notes_field = Entry(inp_frame, font=('arial', 9), textvariable=notes_txt)
    notes_field.grid(row=6, column=1)

    l9 = Label(bot_frame, text="Payment Method")
    l9.grid(row=7, column=0, ipady=2)
    b1 = Radiobutton(bot_frame, text="Cash", value=11)
    b2 = Radiobutton(bot_frame, text="Card", value=12)
    b3 = Radiobutton(bot_frame, text="UPI", value=13)
    b4 = Radiobutton(bot_frame, text="Netbanking", value=14)
    b1.grid(row=7, column=1, ipadx=2)
    b2.grid(row=7, column=2, ipadx=2)
    b3.grid(row=7, column=3, ipadx=2)
    b4.grid(row=7, column=4, ipadx=2)

def home_func():
    # create a frame for display of balance
    main_disp_frame = Frame(window, height=200, width=500, bg='green')
    main_disp_frame.pack(side=TOP)

    h1 = Label(main_disp_frame, text="Your Finance System", font=('arial', 20, 'bold'), justify=CENTER)
    h1.grid(row=0, column=1, ipady=6)

    bt1 = Button(main_disp_frame, text="Show Balance")
    bt1.grid(row=5, column=1, pady=4)

    bt2 = Button(main_disp_frame, text="Add New Entry", command=new_entry)
    bt2.grid(row=3, column=1,pady=4)

    bt3 = Button(main_disp_frame, text="Home", command=home_func)
    bt3.grid(row=7, column=1,pady=4)



if __name__ == '__main__':
    from tkinter import *

    # main window configuration
    window = Tk()
    window.geometry("500x375")
    window.resizable(0, 0)
    window.title("My Finance Tracker")

    bal = 0
    home_func()


    window.mainloop()


