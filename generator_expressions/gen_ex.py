# Iterable is a "sequence" of data, you can iterate over using a loop.
print(hasattr(str, "__iter__")) # Iterable
print(hasattr(bool, "__iter__")) # Not iterable

simple_list=[1,2,3]
my_iterator = iter(simple_list)
print(my_iterator)

# Generators provide a convenient way to implement the iterator protocol
# Generator is an iterable created using a function with a yield statement
# The main feature of generator expression is evaluating the elements on demand.
def my_gen():
    for x in range(5):
        yield x

# Generator expression allows creating a generator on the fly without a yield keyword
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)

for x in gen_exp:
    print(x)

list_comp = [x ** 2 for x in range(10) if x % 2 == 0]

print(list_comp)
print(gen_exp)

# main advantage of generator over a list is that it takes much less memory

sum(i*i for i in range(10))

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))

# 100000 elements in memory first, then sum
total = sum([x**2 for x in range(100000)])

# only one value in memory at a time 
total = sum(x**2 for x in range(100000))

# generator is for single-use
gen = (x for x in range(3))
print(list(gen)) # [0,1,2]
print(list(gen)) # [] - empty

