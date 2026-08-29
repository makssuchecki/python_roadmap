# os module
# This module has functions to perform tasks of operating system

import os

# os.mkdir("./hello")

print(os.getcwd())

os.listdir("./")

# random module
# Defies various functions for handling randomization

import random

print(random.random())

print(random.randint(1, 100))

print(random.choice(["computer", "phone"]))

nums = [1, 2, 3, 4]
random.shuffle(nums)
print(nums)

# math module
# Presents commonly required mathematical functions

import math

print(math.pi)

print(math.e)

print(math.sqrt(100))

print(math.ceil(4.59))

print(math.floor(1.9))

# sys module
# Provides functions and variables used to manipulate different of the python runtime environment

import sys

# print("My name is {}. I am {} years old".format(sys.argv[1], sys.argv[2]))

print(sys.maxsize)

print(sys.path)

# collections module

import collections

d = collections.OrderedDict()
d['A'] = 20
d['B'] = 30
d['C'] = 40
for k,v in d.items():
    print(k,v)

q=collections.deque([10, 20, 30, 40])
q.appendleft(110)
q.append(41)
q.pop()
q.popleft()
print(q)

# statistics module
# Provides statistical function

import statistics

print(statistics.mean([2, 5, 7, 8]))

print(statistics.median([1, 4, 6, 2, 6]))

print(statistics.stdev([5.5, 2.9, 6.1, 5.9]))

# Time module
# Has many time related functions

import time 

print(time.time())

ct = time.time()

rt = time.localtime(ct)

print(time.asctime(rt))

time.sleep(1)

print(time.ctime())