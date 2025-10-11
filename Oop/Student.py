class Student:

    def __init__(self , name , marks):
        self.name =  name 
        self.marks = marks

    def avg(self):
        val = 0
        count = 0
        for i in self.marks:
            val = +i
            count=+1
        return val/count
    

