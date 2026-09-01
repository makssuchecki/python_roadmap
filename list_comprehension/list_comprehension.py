# List comprehension 
vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]

# 1
squares = []
for i in range(10):
    squares.append(i**2)

# 2 
squares = list(map(lambda x: x**2, range(10)))

# 3
squares = [x**2 for x in range(10)]

combs1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

combs2 = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs2.append((x, y))

# Nested List Comprehensions

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
# transposition
[[row[i] for row in matrix] for i in range(4)]

# equivalent to:
transposed=[]
for i in range(4):
    transposed.append([row[i] for row in matrix])

# or
list(zip(*matrix))

list_comp = [x for x in range(10)]
print(list_comp)