from tkinter import *

# globally declare the expression variable
expression=''
# function to update the expression
# in the text entry text box
def press(num):
    # point out the global expression variable
    global expression
    # concatenation of the string
    expression=expression+str(num)
    # update the expression by using set method
    equation.set(expression)


def equalpress():
    # try and except statemet for handling the errors like zerro 
    # division
    # Put that code inside try block 
    # which may cause errors
    try:
        global expression
        # eval func evaluate the expression
        # and str function convert the result
        # into string
        total=str(eval(expression))
        equation.set(total)

        # initialize the expression variable by empty string
        expression=''
    # if error is generated then handle 
    # by the except block
    except:
        equation.set('error')
        expression=''
# Function to clear the contents of the text entry box
def clear():
    global expression
    expression=''
    equation.set("")


# driver code 
if __name__=='__main__':
    gui=Tk()
    # set background color fro GUI window
    gui.configure(background='LIght green')
    # set title
    gui.title('SImple Calculator')

    # set the configuration of GUI window
    gui.geometry('270x150')

    # stringVar()is the variable class 
    # we create an instance of this class
    equation=StringVar()
    # create the text entry box for 
    # showing the expression
    expresion_field=Entry(gui,textvariable=equation)

    # grid method is used for placing 
    # widgets at the respective positions
    # in table like structure
    expresion_field.grid(columnspan=4,ipadx=70)

    # create a button and place at a particular
    # location inside the root window
    # when user press button , the command/function
    # affiliated to that button is executed.

    button1=Button(gui,text='1',fg='black',bg='red',command=lambda:press(1),height=1,width=7)
    button1.grid(row=2,column=0)

    button2=Button(gui,text='2',fg='black',bg='red',command=lambda:press(2),height=1,width=7)
    button2.grid(row=2,column=1)

    button3=Button(gui,text='3',fg='black',bg='red',command=lambda:press(3),height=1,width=7)
    button3.grid(row=2,column=2)

    button4=Button(gui,text='4',fg='black',bg='red',command=lambda:press(4),height=1,width=7)
    button4.grid(row=3,column=0)

    button5=Button(gui,text='5',fg='black',bg='red',command=lambda:press(5),height=1,width=7)
    button5.grid(row=3,column=1)

    button6=Button(gui,text='6',fg='black',bg='red',command=lambda:press(6),height=1,width=7)
    button6.grid(row=3,column=2)

    button7=Button(gui,text='7',fg='black',bg='red',command=lambda:press(7),height=1,width=7)
    button7.grid(row=4,column=0)

    button8=Button(gui,text='8',fg='black',bg='red',command=lambda:press(8),height=1,width=7)
    button8.grid(row=4,column=1)

    button9=Button(gui,text='9',fg='black',bg='red',command=lambda:press(9),height=1,width=7)
    button9.grid(row=4,column=2)

    button0=Button(gui,text='0',fg='black',bg='red',command=lambda:press(0),height=1,width=7)
    button0.grid(row=5,column=0)

    plus=Button(gui,text='+',fg='black',bg='red',command=lambda:press('+'),height=1,width=7)
    plus.grid(row=2,column=3)

    minus=Button(gui,text='-',fg='black',bg='red',command=lambda:press('-'),height=1,width=7)
    minus.grid(row=3,column=3)

    multiply=Button(gui,text='*',fg='black',bg='red',command=lambda:press('*'),height=1,width=7)
    multiply.grid(row=4,column=3)

    divide=Button(gui,text='/',fg='black',bg='red',command=lambda:press('/'),height=1,width=7)
    divide.grid(row=5,column=3)

    # clear
    delete=Button(gui,text='Clear',fg='black',bg='red',command=lambda:clear(),height=1,width=7)
    delete.grid(row=5,column=1)

    # equal=
    equal=Button(gui,text='=',fg='black',bg='red',command=lambda:equalpress(),height=1,width=7)
    equal.grid(row=5,column=2)

    # decimal=Button()
    decimal=Button(gui,text='.',fg='black',bg='red',command=lambda:press('.'),height=1,width=7)
    decimal.grid(row=6,column=0)
    # start the GUI
    gui.mainloop()
