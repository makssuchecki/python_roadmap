
# Example 1
# A decorator takes a function, extends it and returns
def hello(func):
    def inner():
        print("Hello ")
        func()
    return inner

def name():
    print("Alice")

obj = hello(name)
obj()

# Example 2
# Functions can be extended by wrapping them
def who():
    print("Alice")

def display(func):
    def inner():
        print("The current user is : ", end="")
        func()
    return inner

if __name__ == "__main__":
    myobj = display(who)
    myobj()

# Python can simplify the use of decorators with the @ symbol
@hello
def name():
    print("Alice")

if __name__ == "__main___":
    name()

# Parameters can be used with decorators
def sumab(a, b):
    summed = a + b
    print(summed)

def pretty_sumab(func):
    def inner(a, b):
        print(str(a) + " + " + str(b) + " is ", end="")
        return func(a,b)
    return inner

@pretty_sumab
def sumab(a, b):
    summed = a + b
    print(summed)

if __name__ == "__main__":
    sumab(5, 3)

# Real world examples

# Time measurement 
import time
def measure_time(func):
    def wrapper(*arg):
        t = time.time()
        res = func(*arg)
        print("Function took " + str(time.time()-t) + " seconds to run")
    return wrapper

@measure_time
def myFunction(n):
    time.sleep(n)

if __name__ == "__main__":
    myFunction(2)

# Web apps
# in flask @app.route("/") is a decorator

# @app.route("/about")
# def about_page():
#     return "Website about nachos"