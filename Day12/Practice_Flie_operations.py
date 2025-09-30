# Script to open the file and write 10 lines to it and print the lines in new line

# opening file as write mode to write
try :
    with open("example.txt" , 'w') as file :
        for i in range(10) :
            file.write(f'Adding {i} line in this file from script\n')

# if file is not found try will return a error which should print below

except FileNotFoundError:
    print("Seems like file Doesn't exists try again or enter correct filename")

# Reading the file to print it

try :
    with open('example.txt' , 'r') as reading_file :
        lines = reading_file.readlines()
        for line in lines:
            print(line.strip())
except FileNotFoundError :
    print('unable to read the file check the file name again')

try :
    with open('example.txt' , 'r') as reading_file :
        lines = reading_file.readlines()
        for line in lines:
            if '1' in line:
                print(f'1 is peresent in the above text file')
except FileNotFoundError :
    print('unable to read the file check the file name again')
