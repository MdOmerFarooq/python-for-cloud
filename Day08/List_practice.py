my_list = [1,2,9,6,1,3,4,5]   # Declaring list

print(len(my_list))  # printng lengh of the list

# Sorting the list using sort functions

my_list.sort()
print("sorted list" , my_list )

# adding an element to the list 

my_list.append(6)  
print("after appending" , my_list)  # prining the list after apppending

# Removing an element From the list 

my_list.remove(6)
print("after removing" , my_list) # prining the list after Removing

# Slicing the list 

print('sliced list' , my_list[0:4])

# Practicing in operator

if 1 in my_list :
    print("yes")

# creating a new list and learning the sorted() 

new_list = [2,1,5,3,4,9]
print('new list', new_list)
sorted_list = sorted(new_list)  # sorted is an another list where unless like .sort() method it does not return none instead returns the sorted list 
print('sorted new list ' , sorted_list)

