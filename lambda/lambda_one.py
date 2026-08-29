def identity(x):
    return x


lambda x: x
# keyword: lambda
# bound variable: x
# body: x


(lambda x: x + 1)(2)

add_one = lambda x: x + 1
print(add_one(2))

full_name = lambda first, last: f"Full name: {first.title()} {last.title()}"
print(full_name('max', 'suchecki'))

# Anonymous function is a function without a name

lambda x, y: x + y

# Immediately Invoked Function Expression
print((lambda x, y: x+y)(2, 3))

high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))

(lambda x, y, z: x + y + z)(1, 2, 3)

(lambda x, y, z=3: x + y + z)(1, 2)

(lambda x, y, z=3: x + y + z)(1, y=2)

(lambda *args: sum(args))(1, 2, 3)

(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)

(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)

# Decorators
# is the implementation of a pattern that allows adding a behavior
# to a function or a class

def some_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)
    return wraps

@some_decorator
def decorated_function(x):
    print(f"With argument: '{x}'")

decorated_function("Python")


def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)
    return wrap

@trace
def add_two(x):
    return x+2
add_two(3)

# a decorator can be applied to a lambda
print((trace(lambda x: x ** 2))(3))

list(map(trace(lambda x: x*2), range(3)))

# Closure
# is a function where every free variable is bound to a specific value
# defined in the enclosing scope of that function

def outer_func(x):
    y = 4
    def inner_func(z):
        print(f"x = {x}, y={y}, z={z}")
        return x + y + z
    return inner_func
for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")

# lambda can also be a closure
def outer_func(x):
    y = 4
    return lambda z: x + y + z

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")



def wrap(x):
    def f():
        print(n)
    return f

numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(wrap(n))

for f in funcs:
    f()


for n in numbers:
    funcs.append(lambda n=n: print(n))

for f in funcs:
    f()

import unittest

addtwo = lambda x: x + 2

class LambdaTest(unittest.TestCase):
    def test_add_two(self):
        self.assertEqual(addtwo(2), 4)

    def test_add_two_point_two(self):
        self.assertEqual(addtwo(2.2), 4.2)



if __name__ == '__main__':
    unittest.main(verbosity=2)


addtwo = lambda x: x + 2
addtwo.__doc__ = """Add 2 to a number
    >>> addtwo(2)
    4
    >>> addtwo(2.2)
    4.2
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)