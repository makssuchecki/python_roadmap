# Local Scope
def myfunc():
    x = 300
    print(x)
myfunc()

def myfunctwo():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()


# Global Scope
x = 300
def myfunc():
    print(x)
myfunc()

print(x)

# if you need to create a global variable
# but are stuck in the local scope use global keyword
def myfunc():
    global x
    x = 200

myfunc()

print(x)

# the nonlocal keyword is used to work with variables inside nested functions
def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x 
        x = "hello"
    myfunc2()
    return x
print(myfunc1())

# LEGB Rule
# Python follows the LEGB rule when looking up variable names
# and searches in order:
# 1. Local - inside current function
# 2. Enclosing - inside enclosing functions (from inner to outer)
# 3. Global - at the top level of the module
# 4. Built-in - In Python's built-in namespace

x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner:", x)
    inner()
    print("Outer:", x)
outer()
print("Global:", x)

# example of counter using nonlocal
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1 
        return count
    return increment

counter = make_counter()

print(counter())
print(counter())
print(counter())

# Memoization
def memoized_square():
    cache = {}
    def square(n):
        nonlocal cache
        if n not in cache:
            cache[n] = n * n
        return cache[n]
    return square

# Managing shared state in closures
def toggle_flag():
    enabled = False
    def toggle():
        nonlocal enabled
        enabled = not enabled
        return enabled
    return toggle

# Avoiding global in small utilities
def request_tracker():
    total = 0
    def track():
        nonlocal total
        total += 1
        return total   
    return track