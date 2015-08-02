__author__ = 'sco-lo-digital'
#create a function for each of the 5 menu options
#Option 1 - Addition
def Add(x, y):
    summation= x + y
    return print('%d + %d = ' %(x,y), summation)
#Option 2 - Subtraction
def Sub(x, y):
    subtraction = x - y
    return print('%d - %d = ' %(x,y), subtraction)
#Option 3 - Multiplication
def Mult(x, y):
    multiply = x * y
    return print('%d * %d = ' %(x,y), multiply)
    #Option 4 - Division
def Div(x, y):
    divide = x/ y
    return print('%d / %d = ' %(x,y), divide)
    #Option 5 - Remainder
def Rem(x, y):
    remainder = x % y
    return print("%d remainder %d = " %(x,y), remainder)
    #create string variable avail_operators
avail_operators = '+,-,*,/,%'
#prompt the user to enter an expression using operator in 1-5
expression = input('Please enter the expression you would like calculated using an operation from the menu 1-5. ie. 13+54')

#implement and invoke function Evaluate(), argument type string
def Evaluate(x):
    x=str(x)
    #parse the string to search for the operators
    op = min(x)
    if op in avail_operators != True:
        print('You have entered an invalid operator.')
        quit()
    #position in the string of the operator
    pos = x.find(op)
    #extract operands
    operand1 = float(x[:pos])
    operand2 = float(x[pos+1:])
    #identify and store the location of op in available_operators
    indexpos = avail_operators.find(op)
    #invoke the function that performs the required calculation
    if indexpos == 0:
        Add(operand1,operand2)
    elif indexpos == 2:
        Sub(operand1,operand2)
    elif indexpos == 4:
        Mult(operand1, operand2)
    elif indexpos == 6:
        Div(operand1, operand2)
    elif indexpos == 8:
        Rem(operand1, operand2)
    else:
        print('You did not enter a valid operator')
        quit()


print (Evaluate(expression))



    # for i in expression:
    #     #pos = expression.find(i)
    #     print(i)

#
#
#exractcs operands
#alerts user to missing operand
#handles unexpected input from user

#calculate and print result to user