## calculator program but with command line args 

import sys  # sys is the module which makes command line args possible 
import my_module as module

num1 = float(sys.argv[1])  # argv is function that reads the input . 
num2 = float(sys.argv[2])  # by default it reads input as str thus you need to convert it
operation = sys.argv[3]

if operation == 'add' or operation == '+':
    print(f'{operation} of {num1} and {num2} is :' , module.add(num1 , num2))  
elif operation == 'Subtract' or operation == '-':
    print(f'{operation} of {num1} and {num2} is : ' , module.sub(num1 , num2))
elif operation == 'multiply' or operation == '*':
    print(f'{operation} of {num1} and {num2} is : ' , module.mul(num1 , num2))
elif operation == 'Divide' or operation == '/':
    print(f'{operation} of {num1} and {num2} is : ' , module.div(num1 , num2))
else :
    print(f'{operation} is an inccorrect operation')


 