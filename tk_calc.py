#********************************************************************#
"""
Title:         Python Basic Calculator Program
Author:        Kaiju
"""
#********************************************************************#
from tkinter import *

# creating the basic calculator window
window = Tk()
window.geometry("312x334") # size of window: width=312, height=334
window.resizable(1, 1)
window.title("Python Calculator")

#********************************************************************#
# btn_click function continuously updates the input field when you enter a number
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_txt.set(expression)

# btn_clear clears the input field
def btn_clear():
    global expression, prev_calc
    expression = ""
    input_txt.set("")
    prev_calc = ""
    output_txt.set("")

# btn_equal calculates the expression present in input field
# it also displays the previous calculations in the topmost bar
def btn_equal():
    global expression, result, prev_calc
    prev_calc += expression
    if (expression[0].isnumeric() or expression[0] == "."):
        result = str(eval(expression)) # 'eval' function evalauates the expression directly
    else:
        exp1 = result + expression
        result = str(eval(exp1))  # 'eval' function evalauates the expression directly
    output_txt.set(prev_calc)
    input_txt.set(result)
    expression = ""




expression = ""
prev_calc = ""
# 'StringVar()' is used to get the instance of input field
input_txt = StringVar()
output_txt = StringVar()

# creating a frame for previous calculations
prev_frame = Frame(window, width=312, height=25, bg="#eee")
prev_frame.pack(side=TOP)

# creating output field inside the Frame
prev_field = Entry(prev_frame, font = ('arial', 6), textvariable = output_txt, width=312, bg="#eee", bd=0, justify = RIGHT)
prev_field.grid(row=0, column=0)
prev_field.pack()

# creating a frame for the input field
input_frame = Frame(window, width=312, height=50, bd=0, highlightbackground = 'black', highlightcolor = 'black', highlightthickness = 1)
input_frame.pack(side=TOP)

# creating input field inside the Frame
input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_txt, width=50, bg="#eee", bd=0, justify = RIGHT)
input_field.grid(row=1, column=0)
input_field.pack(ipady = 10) # 'ipady' is internal padding to increase he height of input field


# creating another 'Frame' for the buttons below the 'input_frame'
btns_frame = Frame(window, width=312, height=250, bg="#aaa")
btns_frame.pack()

# first row
clear = Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

# second row
nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("9")).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("8")).grid(row=1, column=1, padx=1, pady=1)
seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("7")).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

# third row
six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("6")).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("5")).grid(row=2, column=1, padx=1, pady=1)
four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("4")).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

# forth row
three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("3")).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("2")).grid(row=3, column=1, padx=1, pady=1)
one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("1")).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

# fifth row
zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("0")).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
dot = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=btn_equal).grid(row=4, column=3, padx=1, pady=1)

window.mainloop()