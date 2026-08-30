# Iterators are methods that iterate collections like lists, tuples, etc
# Using an iterator method we can loop through an object and return its elements

s = "abc"
it = iter(s)

print(next(it)) # a
print(next(it)) # b 
print(next(it)) # c


# An iterator object must implement two special methods
# __iter__() and __next__() collectively called the iterator protocol

class PowTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

numbers = PowTwo(3)

i = iter(numbers)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i)) raise StopIterationException

for i in PowTwo(3):
    print(i)

# Infinite iterators
from itertools import count
infinite_iterator = count(1)
for i in range(5):
    print(next(infinite_iterator))