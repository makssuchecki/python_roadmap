# Encapsulation 
# practice of hiding a class's internal details
# and exposing only what is necessary to prevent accidental modification

class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property # turns into a property
    def Name(self): # getter
        return self.__name

    @Name.setter
    def Name(self, value): # setter
        if value == "Bob":
            self.__name = "Default Name"
        else:
            self.__name = value

    @staticmethod 
    def mymethod():
        print("Hello World")

Person.mymethod()

p1 = Person("Mike", 20, 'm')
print(p1.Name)
p1.Name = "Bob"
print(p1.Name)

p1.mymethod()

# Public 
# accessible anywhere in the code

# Protected 
# intended for use within the class and its subclasses

# Private
# Only accessible within the class that defines them
class Human:
    def __init__(self):
        self.name = "Cess" # Public 

        self._age = 25 # Protected

        self.__ssn = "012-34-5678" # Private

