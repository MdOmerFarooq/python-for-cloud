#lets write a simple calculator program using functions

print('*******welcome to calculator*********')
print('Enter your first number : ')
num1 = int(input('>'))  # by default input is in str so we need to convert it to int so use int()
print('Great choice ! now Enter your Second number number : ')
num2 = int(input('>'))

# funtion to add

def addition():             # def is a keyword used to define a funtion . 
    result = num1 + num2    # Result is a local variable which means you can use this inside the function only
    return result           # returns the value whenever funtion is called 

# funtion to Subtract

def subtraction():
    result = num1 - num2    
    return result 

# funtion to multiply

def multiplication():
    result = num1 * num2    
    return result 

# funtion to Divide

def division():
    result = num1 / num2    
    return result 

# Let's call the functions and print the values .

print(f'Addition of {num1} & {num2} is : {addition()}')   # calling function using function name
print(f'Subtrction of {num1} & {num2} is : {subtraction()}')
print(f'Multiplication of {num1} & {num2} is : {multiplication()}')
print(f'Division of {num1} & {num2} is : {division()}')