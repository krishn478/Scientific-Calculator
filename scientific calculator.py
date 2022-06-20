from tkinter import *
import math

expression = ""
def press(num):
 global expression
 expression = expression + str(num)
 equation.set(expression)
def equalpress():
 try:

  global expression
  total = str(eval(expression))

  equation.set(total)
  expression = ""
 except:

  equation.set(" error ")
  expression = ""
def clear():
 global expression
 expression = ""
 equation.set("")


def sin():
    current = math.sin(math.radians(float(expression)))
    equation.set(current)
def cos():
    current = math.cos(math.radians(float(expression)))
    equation.set(current)
def tan():
    current = math.tan(math.radians(float(expression)))
    equation.set(current)
def acosh():
    current = math.acosh(math.radians(float(expression)))
    equation.set(current)
def asinh():
    current = math.asinh(math.radians(float(expression)))
    equation.set(current)
def atanh():
    current = math.atanh(math.radians(float(expression)))
    equation.set(current)
def log():
    current = math.log(float(expression))
    equation.set(current)
def log2():
    current = math.log2((float(expression)))
    equation.set(current)
def log10():
    current = math.log10(float(expression))
    equation.set(current)
def pi():
    current = math.pi
    equation.set(current)
def tau():
    current = math.tau
    equation.set(current)
def exp():
    current = math.exp(float(expression))
    equation.set(current)
def squared():
    current = math.sqrt(float(expression))
    equation.set(current)
def pm():
    current = -(float(expression))
    equation.set(current)
def factorial():
    current = math.factorial(float(expression))
    equation.set(current)



if __name__ == "__main__":
 gui = Tk()
 gui.configure(background="#fab4b4")
 gui.title("Calculator")
 gui.geometry("280x240")
 equation = StringVar()
 expression_field = Entry(gui, textvariable=equation)
 expression_field.grid(columnspan=4, ipadx=75)

 button1 = Button(gui, text=' 1 ', fg='white', bg='black',
     command=lambda: press(1), height=1, width=7)
 button1.grid(row=2, column=0)

 button2 = Button(gui, text=' 2 ', fg='white', bg='black',
     command=lambda: press(2), height=1, width=7)
 button2.grid(row=2, column=1)

 button3 = Button(gui, text=' 3 ', fg='white', bg='black',
     command=lambda: press(3), height=1, width=7)
 button3.grid(row=2, column=2)

 button4 = Button(gui, text=' 4 ', fg='white', bg='black',
     command=lambda: press(4), height=1, width=7)
 button4.grid(row=3, column=0)

 button5 = Button(gui, text=' 5 ', fg='white', bg='black',
     command=lambda: press(5), height=1, width=7)
 button5.grid(row=3, column=1)

 button6 = Button(gui, text=' 6 ', fg='white', bg='black',
     command=lambda: press(6), height=1, width=7)
 button6.grid(row=3, column=2)

 button7 = Button(gui, text=' 7 ', fg='white', bg='black',
     command=lambda: press(7), height=1, width=7)
 button7.grid(row=4, column=0)

 button8 = Button(gui, text=' 8 ', fg='white', bg='black',
     command=lambda: press(8), height=1, width=7)
 button8.grid(row=4, column=1)

 button9 = Button(gui, text=' 9 ', fg='white', bg='black',
     command=lambda: press(9), height=1, width=7)
 button9.grid(row=4, column=2)

 button0 = Button(gui, text=' 0 ', fg='white', bg='black',
     command=lambda: press(0), height=1, width=7)
 button0.grid(row=5, column=0)

 plus = Button(gui, text=' + ', fg='white', bg='black',
    command=lambda: press("+"), height=1, width=7)
 plus.grid(row=2, column=3)

 minus = Button(gui, text=' - ', fg='white', bg='black',
    command=lambda: press("-"), height=1, width=7)
 minus.grid(row=3, column=3)

 multiply = Button(gui, text=' * ', fg='white', bg='black',
     command=lambda: press("*"), height=1, width=7)
 multiply.grid(row=4, column=3)

 divide = Button(gui, text=' / ', fg='white', bg='black',
     command=lambda: press("/"), height=1, width=7)
 divide.grid(row=5, column=3)

 equal = Button(gui, text=' = ', fg='white', bg='black',
    command=equalpress, height=1, width=7)
 equal.grid(row=9, column=2)

 Decimal= Button(gui, text='.', fg='white', bg='black',
     command=lambda: press('.'), height=1, width=7)
 Decimal.grid(row=6, column=0)
 sin = Button(gui,text='sin',fg='white',bg='black',height=1,width=7,
              command=sin)
 sin.grid(row=5, column='1')
 cos =Button(gui, text='cos',fg= 'white',bg='black',
             command=cos,height=1,width=7)
 cos.grid(row=5,column='2')
 tan =Button(gui,text='tan',fg='white',bg='black',
             command=tan,height=1,width=7)
 tan.grid(row=7,column='1')
 acosh=Button(gui,text='sec',fg='white',bg='black',
             command=acosh,height=1,width=7)
 acosh.grid(row=6,column='1')
 asinh=Button(gui,text='cosec',fg='white',bg='black',
                  command=asinh,height=1,width=7)
 asinh.grid(row=6,column='2')
 atanh =Button(gui,text='cot',fg='white',bg='black',
                    command=atanh,height=1,width=7)
 atanh.grid(row=7,column='2')
 log2 =Button(gui,text='log2',fg='white',bg='black',
             command=log2,height=1,width=7)
 log2.grid(row=6,column='3')
 log10 =Button(gui,text='log10',fg='white',bg='black',
               command=log10,height=1,width=7)
 log10.grid(row=7,column='3')
 clear = Button(gui, text='Clear', fg='white', bg='black',
                command=clear, height=1, width=7)
 clear.grid(row=9, column='3')
 pi =Button(gui,text='pi',fg='white',bg='black',
            command=pi,height=1,width=7)
 pi.grid(row=8,column='3')
 tau =Button(gui,text='2pi',fg='white',bg='black',
            command=tau,height=1,width=7)
 tau.grid(row=8,column='2')
 exp = Button(gui, text='exp', fg='white', bg='black',
                command=exp, height=1, width=7)
 exp.grid(row=8, column='1')
 squared =Button(gui,text='\u221A',fg='white',bg='black',
                 command=squared,height=1,width=7)
 squared.grid(row=7,column='0')
 pm =Button(gui,text=chr(177),fg='white',bg='black',
            command=pm,height=1,width=7)
 pm.grid(row=8,column='0')
 log =Button(gui,text='log',fg='white',bg='black',
             command=log,height=1,width=7)
 log.grid(row=9,column=0)
 factorial =Button(gui,text='factorial',fg='white',bg='black',
                   command=factorial,height=1,width=7)
 factorial.grid(row=9,column=1)




 gui.mainloop()