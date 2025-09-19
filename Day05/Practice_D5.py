import my_module as module  # importing my_module.py file available in this folder to re use the functions available inside it 

num1 = 55
num2 = 66

print(f'Additon of {num1}{num2} is : {module.add(num1 , num2)}')
print(f'Subtraction of {num1}{num2} is : {module.sub(num1 , num2)}')
print(f'Multiplication of {num1}{num2} is : {module.mul(num1 , num2)}')
print(f'Division of {num1}{num2} is : {module.div(num1 , num2)}')


