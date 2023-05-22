from tkinter import *


def buttonClearPressed():
    global operation
    global number1
    operation = ""
    number1 = 0
    answerBox.delete(0, END)


def buttonNumberPressed(number):
    key = answerBox.get()+number
    answerBox.delete(0, END)
    answerBox.insert(0, key)


def buttonAddPressed():
    global operation
    global number1
    operation = "+"
    if answerBox.get() == "":
        number1 = 0.0
    else:
        number1 = float(answerBox.get())
    answerBox.delete(0, END)


def buttonSubtractPressed():
    global operation
    global number1
    operation = "-"
    if answerBox.get() == "":
        number1 = 0.0
    else:
        number1 = float(answerBox.get())
    answerBox.delete(0, END)


def buttonMultiplyPressed():
    global operation
    global number1
    operation = "*"
    if answerBox.get() == "":
        number1 = 0.0
    else:
        number1 = float(answerBox.get())
    answerBox.delete(0, END)


def buttonDividePressed():
    global operation
    global number1
    operation = "/"
    if answerBox.get() == "":
        number1 = 0.0
    else:
        number1 = float(answerBox.get())
    answerBox.delete(0, END)


def buttonEqualToPressed():
    global operation
    global number1
    if answerBox.get() == "":
        number2 = 0.0
    else:
        number2 = float(answerBox.get())
    if operation == '+':
        number1 = number1 + number2
    elif operation == '-':
        number1 = number1 - number2
    elif operation == '/':
        if number2 != 0:
            number1 = number1 / number2
    elif operation == '*':
        number1 = number1 * number2

    answerBox.delete(0, END)
    if operation == '/' and number2 == 0:
        answerBox.insert(0, 'ERRO DIVISÃO POR ZERO')
    else:
        answerBox.insert(0, str(number1))
    operation = ""


calcWindow = Tk()
calcWindow.title('Very Simple Calculator')
calcWindow.iconbitmap('calculator.ico')
'''
Calibri
Comic Sans MS
Consolas
Courier New
System
TNG Monitors
Terminal
Verdana
'''
operation = ""
number1 = 0

answerBox = Entry(calcWindow, width=19, borderwidth=2, justify='right', font=('Consolas 25'))
answerBox.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

button0 = Button(calcWindow, text='0', width=9, height=2, font=('Consolas 20'), bg='light grey', command=lambda: buttonNumberPressed('0'))
button1 = Button(calcWindow, text='1', width=4, height=2, font=('Consolas 20'), bg='light grey', command=lambda: buttonNumberPressed('1'))
button2 = Button(calcWindow, text='2', width=4, height=2, font=('Consolas 20'), bg='light grey', command=lambda: buttonNumberPressed('2'))
button3 = Button(calcWindow, text='3', width=4, height=2, font=('Consolas 20'), bg='light grey', command=lambda: buttonNumberPressed('3'))
button4 = Button(calcWindow, text='4', width=4, height=2, font=('Consolas 20'), bg='light grey', command=lambda: buttonNumberPressed('4'))
button5 = Button(calcWindow, text='5', width=4, height=2, font=('Consolas 20'), bg='light grey', command=lambda: buttonNumberPressed('5'))
button6 = Button(calcWindow, text='6', width=4, height=2, font=('Consolas 20'), bg='light grey', command=lambda: buttonNumberPressed('6'))
button7 = Button(calcWindow, text='7', width=4, height=2, font=('Consolas 20'), bg='light grey', command=lambda: buttonNumberPressed('7'))
button8 = Button(calcWindow, text='8', width=4, height=2, font=('Consolas 20'), bg='light grey', command=lambda: buttonNumberPressed('8'))
button9 = Button(calcWindow, text='9', width=4, height=2, font=('Consolas 20'), bg='light grey', command=lambda: buttonNumberPressed('9'))

buttonAdd = Button(calcWindow, text='+', width=4, height=2, font=('Consolas 20'), command=buttonAddPressed)
buttonSubtract = Button(calcWindow, text='-', width=4, height=2, font=('Consolas 20'), command=buttonSubtractPressed)
buttonMultiply = Button(calcWindow, text='*', width=4, height=2, font=('Consolas 20'), command=buttonMultiplyPressed)
buttonDivide = Button(calcWindow, text='/', width=4, height=2, font=('Consolas 20'), command=buttonDividePressed)

buttonEqualTo = Button(calcWindow, text='=', width=4, height=8, font=('Consolas 20'), bg='grey', command=buttonEqualToPressed)
buttonDot = Button(calcWindow, text='.', width=4, height=2, font=('Consolas 20'), bg='light grey', command=lambda: buttonNumberPressed('.'))
buttonClear = Button(calcWindow, text='C', width=4, height=2, font=('Consolas 20'), bg='grey', command=buttonClearPressed)

button7.grid(row=1, column=0, padx=1, pady=1)
button8.grid(row=1, column=1, padx=1, pady=1)
button9.grid(row=1, column=2, padx=1, pady=1)
buttonAdd.grid(row=1, column=3, padx=1, pady=1)
buttonClear.grid(row=1, column=4, padx=1, pady=1)

button4.grid(row=2, column=0, padx=1, pady=1)
button5.grid(row=2, column=1, padx=1, pady=1)
button6.grid(row=2, column=2, padx=1, pady=1)
buttonSubtract.grid(row=2, column=3, padx=1, pady=1)

button1.grid(row=3, column=0, padx=1, pady=1)
button2.grid(row=3, column=1, padx=1, pady=1)
button3.grid(row=3, column=2, padx=1, pady=1)
buttonMultiply.grid(row=3, column=3, padx=1, pady=1)

button0.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
buttonDot.grid(row=4, column=2, padx=1, pady=1)
buttonDivide.grid(row=4, column=3, padx=1, pady=1)

buttonEqualTo.grid(row=2, column=4, rowspan=3, padx=1, pady=1)

calcWindow.mainloop()
