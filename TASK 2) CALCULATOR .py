#importing libraries
from tkinter import *
import tkinter as tk
#creating tkinter window
root=Tk()
root.title("CALCULATOR")
root.geometry("370x370")

#setting window's icon
root.iconphoto(False,tk.PhotoImage(file="calculator_icon.png") )
#creating a label where the user's entry and the result will be displayed
result_output=Label(root,width=25,height=2,text="",font=("arial",19),anchor="e")
result_output.pack()

#initializing a null string for user input
value=""
#function to update the calculator input
def output(user_input):
    global value
    value+=user_input
    result_output.config(text=value)
#function to clear the entry
def clear_result():
    global value
    value=""
    result_output.config(text=value)
#function to calculate and display the result
def result():
    global value
    calculate=""
    if value != "":
        try:
            calculate=eval(value)
        except:
            calculate="ERROR"
            value=""
    result_output.config(text=calculate)

#setting calculator's background color
root.configure(bg="khaki1")
#creating buttons for calculator
b1=Button(root,text="C",width=5,height=1,font=("arial",16,'bold'),fg="white",bg="#EE6363",command=lambda : clear_result(),cursor="hand2").place(x=12,y=70)

b2=Button(root,text="/",width=5,height=1,font=("arial",16,'bold'),fg="black",bg="lightskyblue",command=lambda : output("/"),cursor="hand2").place(x=105,y=70)

b3=Button(root,text="%",width=5,height=1,font=("arial",16,'bold'),fg="black",bg="lightskyblue",command=lambda : output("%"),cursor="hand2").place(x=195,y=70)

b4=Button(root,text="*",width=5,height=1,font=("arial",16,'bold'),fg="black",bg="lightskyblue",command=lambda : output("*"),cursor="hand2").place(x=285,y=70)

b5=Button(root,text="7",width=5,height=1,font=("arial",16,'bold'),fg="black",bg="lightskyblue",command=lambda : output("7"),cursor="hand2").place(x=12,y=127)

b6=Button(root,text="8",width=5,height=1,font=("arial",16,'bold'),fg="black",bg="lightskyblue",command=lambda : output("8"),cursor="hand2").place(x=105,y=127)

b7=Button(root,text="9",width=5,height=1,font=("arial",16,'bold'),fg="black",bg="lightskyblue",command=lambda : output("9"),cursor="hand2").place(x=195,y=127)

b8=Button(root,text="-",width=5,height=1,font=("arial",16,'bold'),fg="black",bg="lightskyblue",command=lambda : output("-"),cursor="hand2").place(x=285,y=127)

b9=Button(root,text="4",width=5,height=1,font=("arial",16,'bold'),fg="black",bg="lightskyblue",command=lambda : output("4"),cursor="hand2").place(x=12,y=187)

b10=Button(root,text="5",width=5,height=1,font=("arial",16,'bold'),fg="black",bg="lightskyblue",command=lambda : output("5"),cursor="hand2").place(x=105,y=187)

b11=Button(root,text="6",width=5,height=1,font=("arial",16,'bold'),fg="black",bg="lightskyblue",command=lambda : output("6"),cursor="hand2").place(x=195,y=187)

b12=Button(root,text="+",width=5,height=1,font=("arial",16,'bold'),fg="black",bg="lightskyblue",command=lambda : output("+"),cursor="hand2").place(x=285,y=187)

b13=Button(root,text="1",width=5,height=1,font=("arial",16,'bold'),fg="black",bg="lightskyblue",command=lambda : output("1"),cursor="hand2").place(x=12,y=247)

b14=Button(root,text="2",width=5,height=1,font=("arial",16,'bold'),fg="black",bg="lightskyblue",command=lambda : output("2"),cursor="hand2").place(x=105,y=247)

b15=Button(root,text="3",width=5,height=1,font=("arial",16,'bold'),fg="black",bg="lightskyblue",command=lambda : output("3"),cursor="hand2").place(x=195,y=247)

b16=Button(root,text="0",width=12,height=1,font=("arial",16,'bold'),fg="black",bg="lightskyblue",command=lambda : output("0"),cursor="hand2").place(x=12,y=307)

b17=Button(root,text=".",width=5,height=1,font=("arial",16,'bold'),fg="black",bg="lightskyblue",command=lambda : output("."),cursor="hand2").place(x=195,y=307)

b18=Button(root,text="=",width=5,height=4,font=("arial",16,'bold'),fg="white",bg="#3697f5",command=lambda : result(),cursor="hand2").place(x=285,y=247)

mainloop()