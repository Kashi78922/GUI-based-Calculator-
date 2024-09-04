import tkinter as Tk
from tkinter import *

v = Tk()
v.title("Calculator")
v.geometry("400x600")
v.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = str(eval(equation))  # Perform the calculation
            equation = result  # Update equation with result for further operations
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)

label_result = Label(v, width=24, height=2, text="", font=("arial", 24), bg="#ffffff")
label_result.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

Button(v, text="C", width=5, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#3697f5", command=clear).grid(row=1, column=0, padx=5, pady=5)
Button(v, text="/", width=5, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/")).grid(row=1, column=1, padx=5, pady=5)
Button(v, text="%", width=5, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("%")).grid(row=1, column=2, padx=5, pady=5)
Button(v, text="*", width=5, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*")).grid(row=1, column=3, padx=5, pady=5)

Button(v, text="7", width=5, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7")).grid(row=2, column=0, padx=5, pady=5)
Button(v, text="8", width=5, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8")).grid(row=2, column=1, padx=5, pady=5)
Button(v, text="9", width=5, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9")).grid(row=2, column=2, padx=5, pady=5)
Button(v, text="-", width=5, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-")).grid(row=2, column=3, padx=5, pady=5)

Button(v, text="4", width=5, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4")).grid(row=3, column=0, padx=5, pady=5)
Button(v, text="5", width=5, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5")).grid(row=3, column=1, padx=5, pady=5)
Button(v, text="6", width=5, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6")).grid(row=3, column=2, padx=5, pady=5)
Button(v, text="+", width=5, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+")).grid(row=3, column=3, padx=5, pady=5)

Button(v, text="1", width=5, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1")).grid(row=4, column=0, padx=5, pady=5)
Button(v, text="2", width=5, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2")).grid(row=4, column=1, padx=5, pady=5)
Button(v, text="3", width=5, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).grid(row=4, column=2, padx=5, pady=5)
Button(v, text="=", width=5, height=5, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#fe9037", command=calculate).grid(row=4, column=3, rowspan=2, padx=5, pady=5)

Button(v, text="0", width=11, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).grid(row=5, column=0, columnspan=2, padx=5, pady=5)
Button(v, text=".", width=5, height=2, font=("arial", 18, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).grid(row=5, column=2, padx=5, pady=5)

v.mainloop()
