# you can check the data type using an inbuilt function called type() and also you can convert the dataype into a different data type

str = '42' #although the 43 is number since it is written in '' it is considerd as the string

# lets double confirm that 
print(type(str)) 

# now lets demonstrate converting the str to int values

num = int(str)
# with this the str value sholud be converted to type int as we used int()
# lets double confirm that 
print(type(num))

# similarly we can convert str --> int , int -->str , int --> float , float --> int
# but wait how will Abc will be converted ?
str2 = 'abc'
num2 = int(str2) # ValueError: invalid literal for int() with base 10: 'abc'

# ths is because If the string is numeric (e.g., "123"), it works fine  
# But if the string contains non-digit characters (like "abc"), Python cannot interpret it as an integer, and it raises a ValueError:
# This cannot happen successfully because "abc" is not a valid number in base-10 format.

