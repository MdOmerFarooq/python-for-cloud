'''Qs. Define a Employee class with attributes role, department & salary. This class also a showDetails() method.
Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.'''

class Employee :
    def __init__(self , role , dept , salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self) :
        return self.role , self.dept , self.salary

class Engineer(Employee):
    def __init__(self, name , age) :
        self.name = name
        self.age = age
        super().__init__("engineer","IT","8LPA")

eng1 = Engineer('chinna',60)
print(f"Hi {eng1.name} you are {eng1.age} old and your deails are : {eng1.showDetails()} ")
