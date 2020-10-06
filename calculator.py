from tkinter import *
import numpy as np


calc = Tk()
calc.title("Arnab's Calculator")
calc.configure(background="gray90")
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
def back():
       global string 
       string = string[:-1]
       equation.set(string)
def sin():
    click("sin(")
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




text_display=Entry(calc,font=('arial',20,'bold'),textvariable=equation,bg='pale turquoise1',justify='right',border=30,insertwidth=4).grid(columnspan=9)

btn1=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="7",fg="black",bg="powder blue",command=lambda:click(7)).grid(row=5,column=0,pady=5)
btn2=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="8",fg="black",bg="powder blue",command=lambda:click(8)).grid(row=5,column=1)
btn3=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="9",fg="black",bg="powder blue",command=lambda:click(9)).grid(row=5,column=2)
btn4=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="+",fg="black",bg="powder blue",command=lambda:click("+")).grid(row=3,column=3)
btn5=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="4",fg="black",bg="powder blue",command=lambda:click(4)).grid(row=4,column=0,pady=5)
btn6=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="5",fg="black",bg="powder blue",command=lambda:click(5)).grid(row=4,column=1)
btn7=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="6",fg="black",bg="powder blue",command=lambda:click(6)).grid(row=4,column=2)
btn8=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="-",fg="black",bg="powder blue",command=lambda:click("-")).grid(row=4,column=3)
btn9=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="1",fg="black",bg="powder blue",command=lambda:click(1)).grid(row=3,column=0,pady=5)
btn10=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="2",fg="black",bg="powder blue",command=lambda:click(2)).grid(row=3,column=1)
btn11=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="3",fg="black",bg="powder blue",command=lambda:click(3)).grid(row=3,column=2)
btn12=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="*",fg="black",bg="powder blue",command=lambda:click("*")).grid(row=5,column=3)
btn13=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="/",fg="black",bg="powder blue",command=lambda:click("/")).grid(row=6,column=3)
btn14=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="0",fg="black",bg="powder blue",command=lambda:click(0)).grid(row=6,column=1)
btn15=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="C",fg="white",bg="red2",command=lambda:clear()).grid(row=1,column=1,padx=10)
btn16=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="=",fg="white",bg="green2",command=lambda:equalsTo()).grid(row=1,column=3)
btn17=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text=".",fg="black",bg="powder blue",command=lambda:click(".")).grid(row=6,column=2)
btn18=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="(",fg="black",bg="powder blue",command=lambda:click("(")).grid(row=2,column=2,padx=10)
btn19=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text=")",fg="black",bg="powder blue",command=lambda:click(")")).grid(row=2,column=3,padx=10)
btn20=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="^",fg="black",bg="powder blue",command=lambda:click("^")).grid(row=6,column=0,pady=5)
btn21=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="pi",fg="black",bg="powder blue",command=lambda:click("pi")).grid(row=2,column=0,pady=5)
btn22=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="e",fg="black",bg="powder blue",command=lambda:click("e")).grid(row=2,column=1)
btn23=Button(calc,padx=20,pady=1,width=2,bd=8,font=('arial',20,'bold'),text="Cl",fg="white",bg="red2",command=lambda:back()).grid(row=1,column=0,pady=5,padx=10)



calc.mainloop()
