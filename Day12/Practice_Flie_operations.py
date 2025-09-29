try :
    with open("example.txt" , 'w') as file :
        for i in range(10) :
            file.write(f'Adding {i} line in this file from script\n')
except FileNotFoundError:
    print("Seems like file Doesn't exists try again or enter correct filename")

try :
    with open('example.txt' , 'r') as reading_file :
        lines = reading_file.readlines()
        for line in lines:
            print(line.strip())
except FileNotFoundError :
    print('unable to read the file check the file name again')
