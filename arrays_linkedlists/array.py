# An array is a data structure which can hold more than one value at a time
# It is a collection or unordered series of elements of the same type

import array as arr 
# from array import * <- Alternative

a=arr.array("d",[1.2,1.3,2.3])

# a=arr.array(data type, value list)

print(a[1]) # 1.3

print(len(a)) # 3

a.append(3.4)
print(a)

a.insert(2, 3.7)
print(a)

b=arr.array("d", [0.2, 4.5])
c=arr.array("d")
c=a+b
print("Array c = ", c)

print(a.pop())
print(a.pop(3))
print(a)

print(a[1:3])

print("All values")
for x in a:
    print(x)
