# Defining a class

class Employee:
    def __init__(self,name,desig):
        self.name = name
        self.desig =  desig

emp1 = Employee('Amartya','SE')
emp2 = Employee('Aniket','DEVOPS')

print(emp2.name)


# dog.py

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
