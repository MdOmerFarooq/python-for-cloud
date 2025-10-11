# OOP in Python

To map with real world scenarios, we started using objects in code. This is called object oriented programming.

## Class & Object in Python

Class is a blueprint for creating objects.
```python 
#creating class
class Student:
    name = “karan kumar”
#creating object (instance)
s1 = Student( )   # must be created out of class
print( s1.name ) 
```
## _ _init_ _ Function

All classes have a function called __init__(), which is always executed when the object is being
initiated.
```python 
#creating class
class Student:
    def __init__( self, fullname ):   # Constructor
        self.name = fullname
#creating object
s1 = Student( “karan” )
print( s1.name )
``` 
Note -- > The self parameter is a reference to the current
instance of the class, and is used to access variables
that belongs to the class.

## Methods

Methods are functions that belong to objects.

```python
#creating class 
class Student:
    def __init__( self, fullname ):
        self.name = fullname
    def hello( self ):
        print( “hello”, self.name)

#creating object
s1 = Student( “karan” )
s1.hello( )
```
