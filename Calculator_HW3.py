__author__ = 'sco-lo-pro'
#call the math package
import math

#establish try/except to catch user errors
try:
#welcome user and present main menu
    inp= int(input("Welcome to the calculator! Please select from the following menu;\n"
               "1. Addition\n"
               "2. Subtraction\n"
               "3. Multiplication\n"
               "4. Division\n"
               "5. Power\n"
               "6. Min\n"
               "7. Max\n"
               "8. Square Root\n"
               "9. Exponent\n"
               "10. Sin\n"
                "Please make your selection: "))
#multi-way statement to determine operation
    if inp== 1:
        #instructions for user
        print("The addition Operator needs two operands")
        #create string object to capture operands
        operands=str(input("Please enter two operands, separated by a comma"))
        if operands.find(',')== -1:
            print("Didn't I tell you to enter two operands separated by a comma? Goodbye.")
            quit()
        #extracts location of the comma and creates two placeholders for locations
        pos= operands.find(",")
        #identify location where first operand ends
        pos1= pos
        #identify location where first operand begins
        pos2= pos+ 1
        #extracts numbers from string and converts string to float
        operand1=float(operands[:pos1])
        operand2=float(operands[pos2:])
        #rounds with 3 digits
        result= round(operand1+operand2, 3)
        #returns the result to user
        print("The output of the Addition Operation is: ", result)
    elif inp== 2:
        print("The subtraction Operator needs two operands")
        operands=input("Please enter two operands, separated by a comma")
        if operands.find(',')== -1:
            print("Didn't I tell you to enter two operands separated by a comma? Goodbye.")
            quit()
        pos= operands.find(",")
        pos1= pos
        pos2= pos+ 1
        operand1=float(operands[:pos1])
        operand2=float(operands[pos2:])
        result= round(operand1-operand2, 3)
        print("The output of the Subtraction Operation is: ", result)
    elif inp== 3:
        print("The Multiplication Operator needs two operands")
        operands=input("Please enter two operands, separated by a comma")
        if operands.find(',')== -1:
            print("Didn't I tell you to enter two operands separated by a comma? Goodbye.")
            quit()
        pos= operands.find(",")
        pos1= pos
        pos2= pos+ 1
        operand1=float(operands[:pos1])
        operand2=float(operands[pos2:])
        result= round(operand1*operand2, 3)
        print("The output of the Multiplication Operation is: ", result)
    elif inp== 4:
        print("The Division Operator needs two operands")
        operands=input("Please enter two operands, separated by a comma")
        if operands.find(',')== -1:
            print("Didn't I tell you to enter two operands separated by a comma? Goodbye.")
            quit()
        pos= operands.find(",")
        pos1= pos
        pos2= pos+ 1
        operand1=float(operands[:pos1])
        operand2=float(operands[pos2:])
        result= round(operand1/operand2, 3)
        print("The output of the Division Operation is: ", result)
    elif inp== 5:
        print("The Power Operator needs two operands")
        operands=input("Please enter two operands, separated by a comma")
        if operands.find(',')== -1:
            print("Didn't I tell you to enter two operands separated by a comma? Goodbye.")
            quit()
        pos= operands.find(",")
        pos1= pos
        pos2= pos+ 1
        operand1=float(operands[:pos1])
        operand2=float(operands[pos2:])
        result= round(math.pow(operand1,operand2), 3)
        print("The output of the Power Operation is: ", result)
    elif inp== 6:
        print("The Min Operator needs two operands")
        operands=input("Please enter two operands, separated by a comma")
        if operands.find(',')== -1:
            print("Didn't I tell you to enter two operands separated by a comma? Goodbye.")
            quit()
        pos= operands.find(",")
        pos1= pos
        pos2= pos+ 1
        operand1=float(operands[:pos1])
        operand2=float(operands[pos2:])
        result= round(min(operand1, operand2), 3)
        print("The output of the Min Operation is: ", result)
    elif inp== 7:
        print("The Max Operator needs two operands")
        operands=input("Please enter two operands, separated by a comma")
        if operands.find(',')== -1:
            print("Didn't I tell you to enter two operands separated by a comma? Goodbye.")
            quit()
        pos= operands.find(",")
        pos1= pos
        pos2= pos+ 1
        operand1=float(operands[:pos1])
        operand2=float(operands[pos2:])
        result= round(max(operand1, operand2), 3)
        print("The output of the Max Operation is: ", result)
    elif inp== 8:
        print("The Square Root Operator needs one operand")
        operands=input("Please enter one operand.")
        if operands.find(',')!= -1:
            print("Didn't I tell you to enter ONLY one operand? Goodbye.")
            quit()
        operand1=float(operands)
        result= round(math.sqrt(operand1), 3)
        print("The output of the Square Root Operation is: ", result)
    elif inp== 9:
        print("The Exponent Operator needs one operand")
        operands=input("Please enter one operand.")
        if operands.find(',')!= -1:
            print("Didn't I tell you to enter ONLY one operand? Goodbye.")
            quit()
        operand1=float(operands)
        result= round(math.exp(operand1), 3)
        print("The output of the Exponent Operation is: ", result)
    elif inp== 10:
        print("The Exponent Operator needs one operand")
        operands=input("Please enter one operand.")
        if operands.find(',')!= -1:
            print("Didn't I tell you to enter ONLY one operand? Goodbye.")
            quit()
        operand1=float(operands)
        result= round(math.sin(operand1), 3)
        print("The output of the Sin Operation is: ", result)
    #account for an out of bounds selection from the main menu
    else:
        print("You have entered an invalid Operation. Please try again.")
        quit()
#consider invalid operands
except ValueError:
    print('ERROR: You have to enter valid number. HAVE to.')
    quit()
#consider missing the comma
except IndexError:
    print("I'm guessing you didn't enter your operands separated by a comma. Shame.")
    quit()
#consider invalid operations
except ArithmeticError:
    print("ERROR: Can't divide by zero. And stuff. You know that.")
    quit()
except RuntimeError:
    print("Error: Encountered a Run Time Error.")
    quit()





