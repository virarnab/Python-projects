from tkinter import *
import numpy as np


calc = Tk()
calc.title("Calculator")
calc.configure(background="light green")
equation=StringVar()
string=''

def click(number):
    global string
    string += str(number)
    equation.set(string)

def clear():
    global string
    string = ''
    equation.set(string)

def sin():
    global string
    string = float(string)
    string = round(math.sin(math.radians(string)), 5)
    equation.set(float(string))
    string = str(string)
def good(string):
     if "^" in string:
            string = string.replace("^","**")
  #          equation.set(str(eval(string.replace("^","**"))))
     if "pi" in string:
            string = string.replace("pi",str(np.pi))

#            equation.set(str(eval(string.replace("pi",str(np.pi)))))
     if "e" in string:
            string = string.replace("e",str(np.e))
     if "sin" in string:
            string = string.replace("e",str(np.sin))
     if "cos" in string:
            string = string.replace("e",str(np.cos))
     if "tan" in string:
            string = string.replace("e",str(np.tan))
     if "log" in string:
            string = string.replace("e",str(np.log))
     if "arcsin" in string:
            string = string.replace("e",str(np.arcsin))
     if "arccos" in string:
            string = string.replace("e",str(np.arccos))

     return string
def equalsTo():
    global string
    string = good(string)
    try:
       
#            equation.set(str(eval(string.replace("e",str(np.e)))))
        
        equation.set(str(eval(string)))
    except:
        
        string='Error!'
        equation.set(string)




text_display=Entry(calc,font=('arial',20,'bold'),textvariable=equation,bg='aqua',justify='right',border=30,insertwidth=4).grid(columnspan=9)
btn1=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="7",fg="black",bg="yellow",command=lambda:click(7)).grid(row=1,column=0,padx=10,pady=5)
btn2=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="8",fg="black",bg="yellow",command=lambda:click(8)).grid(row=1,column=1,padx=10)
btn3=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="9",fg="black",bg="yellow",command=lambda:click(9)).grid(row=1,column=2,padx=10)
btn4=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="+",fg="black",bg="yellow",command=lambda:click("+")).grid(row=1,column=3,padx=10)
btn5=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="4",fg="black",bg="yellow",command=lambda:click(4)).grid(row=2,column=0,pady=5)
btn6=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="5",fg="black",bg="yellow",command=lambda:click(5)).grid(row=2,column=1)
btn7=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="6",fg="black",bg="yellow",command=lambda:click(6)).grid(row=2,column=2)
btn8=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="-",fg="black",bg="yellow",command=lambda:click("-")).grid(row=2,column=3)
btn9=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="1",fg="black",bg="yellow",command=lambda:click(1)).grid(row=3,column=0,pady=5)
btn10=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="2",fg="black",bg="yellow",command=lambda:click(2)).grid(row=3,column=1)
btn11=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="3",fg="black",bg="yellow",command=lambda:click(3)).grid(row=3,column=2)
btn12=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="*",fg="black",bg="yellow",command=lambda:click("*")).grid(row=3,column=3)
btn13=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="/",fg="black",bg="yellow",command=lambda:click("/")).grid(row=4,column=0,pady=5)
btn14=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="0",fg="black",bg="yellow",command=lambda:click(0)).grid(row=4,column=1)
btn15=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="C",fg="black",bg="yellow",command=lambda:clear()).grid(row=4,column=2)
btn16=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="=",fg="black",bg="yellow",command=lambda:equalsTo()).grid(row=4,column=3)
btn17=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text=".",fg="black",bg="yellow",command=lambda:click(".")).grid(row=5,column=0,pady=5)
btn18=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="(",fg="black",bg="yellow",command=lambda:click("(")).grid(row=5,column=1)
btn19=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text=")",fg="black",bg="yellow",command=lambda:click(")")).grid(row=5,column=2)
btn20=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="^",fg="black",bg="yellow",command=lambda:click("^")).grid(row=5,column=3)
btn21=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="pi",fg="black",bg="yellow",command=lambda:click("pi")).grid(row=6,column=0,pady=5)
btn22=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="e",fg="black",bg="yellow",command=lambda:click("e")).grid(row=6,column=1)




calc.mainloop()
