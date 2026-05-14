class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_details(self):
        print("----------------------------")
        print(f"Name:{self.name}") 
        print(f"Age:{self.age}")  

    def phone(self):
        print("calling from parent phone")


class Student(Person):
       def study(self):
            print("Study going on")    

       def phone(self):
           print("calling from my own phone")


s1=Student("Sonam","23") # calling parent class construtre  
s1.show_details()  # calling parent class method    
s1.study()   # calling own method         
s1.phone() 











