my_tuple = (1,2,9,6,1,3,4,5)   # Declaring tuple

print(len(my_tuple))  # printng lengh of the tuple

# Sorting the list using sort functions

my_tuple = sorted(my_tuple)
print("sorted tuple" , my_tuple )

# adding an element to the tupole isn't possible because it is immutable 

# Removing an element From the tuple 

my_tuple.remove(6)
print("after removing" , my_tuple) # prining the list after Removing

# Slicing the tuple 

print('sliced tuple' , my_tuple[0:4])

# Practicing in operator

if 1 in my_tuple :
    print("yes")

# Tuple Packing and Unpacking
new_tuple = (1,2)

def tup_var(new_tuple):
    x,y = new_tuple
    print ( x , y)


tup_var(new_tuple)


