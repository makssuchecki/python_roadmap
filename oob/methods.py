# Magic methods are the special methods that start and end with the double underscore
# also called dunder methods

dir(int)
# output
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', 
# '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', 
# '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', 
# '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__','__le__', 
# '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', 
# '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', 
# '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', 
# '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 
# 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 
# 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']

num=10
res = num.__add__(5)
print(res)

# __new__
# is implicitly called before the __init__() method

class Employee:
    def __new__(cls):
        print("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst
    def __init__(self):
        print("__init__ magic method is called")
        self.name='max'

# __str__
# It is overridden to return a printable string representation of any user defined class
num=12
val = int.__str__(num)
print(type(val))

class Employer:
    def __init__(self):
        self.name="max"
        self.salary=0
    def __str__(self):
        return 'Name: '+self.name.title() +", Salary: $"+str(self.salary)
e= Employer()
print(e)

# __add__ 
# used to overload addition

class distance:
    def __init__(self, x=None, y=None):
        self.ft=x
        self.inch=y
    def __add__(self, x):
        temp=distance()
        temp.ft=self.ft+x.ft
        temp.inch=self.inch+x.inch
        if temp.inch >= 12:
            temp.ft+=1
            temp.inch-=12
            return temp
    def __str__(self):
        return 'ft: '+str(self.ft) + " in: "+str(self.inch)
    def __ge__(self, x):
        val1=self.ft*12+self.inch
        val2=x.ft*12+x.inch
        if val1>=val2:
            return True
        else:
            return False
d1=distance(3,10)
d2=distance(4,6)
print("d1={} d2={}".format(d1, d2))
d3= d1+d2
print(d3)

# __ge__
# used to overload >= operator

# def __ge__(self, x):
#     val1=self.ft*12+self.inch
#     val2=x.ft*12+x.inch
#     if val1>=val2:
#         return True
#     else:
#         return False

print(d1>=d2)