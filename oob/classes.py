# Classes provide a means of bundling data and functionality together.
class ClassName:
    # <statement> ... 
    pass

class MyClass:
    def __init__(self):
        self.data = []

    i = 12345
    def f(self):
        return 'hello world'
    
x = MyClass()

xf = x.f
print(xf())

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i

# Data attributes need not to be declared
# like local variables they spring into existence when they are first assigned to

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

class Dog:
    kind = 'canine' # class variable shared by all instances
    def __init__(self, name):
        self.name = name # instance variable unique to each instance

# If the same attribute name occurs in both instance and in a class,
# then attribute lookup prioritizes the instance
class Warehouse:
    purpose = 'storage'
    region = 'west'
w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)

# Methods may call other methods by using method attributes of the self argument
class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)

# Inheritance
class BaseClassName:
    # <statement>
    pass
class DerivedClassName(BaseClassName):
    # <statement>
    pass 

# all methods in Python are effectively virtual

# Multiple Inheritance
class Base1:
    pass
class Base2:
    pass
class Base3:
    pass

class DerivedClassName(Base1, Base2, Base3):
    # <statement>
    pass

# "Private" convention
# a name prefixed with an underscore (e.g. __spam) should be treated as non-public part of the API

# Name mangling
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update

class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)

# Iterator 
class Reverse:
    """Iterator for looping over a sequence backwards"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

# Generators
# Written like regular functions but use the yield statement whenever they want to return data
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

# @staticmethod
class Math:
    @staticmethod
    def add(a, b):
        return a + b

Math.add(2, 3) # 5

# @classmethod
class Employee:
    employee_count = 0
    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

    @classmethod
    def from_string(cls, data):
        name = data.split("-")[0]
        return cls(name)

    @classmethod
    def how_many(cls):
        return cls.employee_count

p = Employee.from_string("Max-Suchecki")
Employee.how_many() # 1