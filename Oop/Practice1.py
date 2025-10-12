# Let's Practice

''' Qs. Define a Circle class to create a circle with radius r using the constructor.
Define an Area() method of the class which calculates the area of the circle.
Define a Perimeter() method of the class which allows you to calculate the perimeter of the
'''

# creating a class 

class Circle:

    def __init__(self , radius):   # constructor which takes radius and creates objects 
        self.radius = radius

    # function to return area of circle .

    def areaOfCircle(self):
        area = 3.14*(self.radius*self.radius) 
        return area
    
    # function to return perimeter of circle

    def perimeterOfCircle(self):
        perimiter = 2*(3.14*self.radius)
        return perimiter
    
# creating the object 

circle1 = Circle(int(input('Enter the radius of the Circle : ')))

# printing the results 

print(f'The area of circle with radius {circle1.radius} is {circle1.areaOfCircle()} and perimter is {round(circle1.perimeterOfCircle(), 2)}')

