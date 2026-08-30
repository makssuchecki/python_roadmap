# Appropriate Uses of Lambda Expressions

# Classic Functional Constructs
list(map(lambda x: x.upper(), ["cat", "dog", "cow"]))

list(filter(lambda x: 'o' in x, ["cat", "dog", "cow"]))

from functools import reduce
reduce(lambda acc, x: f'{acc} | {x}', ["cat", "dog", "cow"])

# Key functions
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
sorted_ids = sorted(ids, key=lambda x: int(x[2:]))

# import tkinter as tk
# import sys

# window = tk.Tk()
# window.grid_columnconfigure(0, weight=1)
# window.title("Lambda")
# window.geometry("300x100")
# label = tk.Label(window, text="Lambda Calculus")
# label.grid(column=0, row=0)
# button = tk.Button(
#     window,
#     text="Reverse",
#     command=lambda: label.configure(text=label.cget("text")[::-1]),
# )
# button.grid(column=0, row=1)
# window.mainloop()

# Python interpreter
from timeit import timeit
timeit("factorial(999)", "from math import factorial", number=10)

from math import factorial
timeit(lambda: factorial(999), number=10)


# Alternatives to Lambdas
# Map
list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))
# using list comprehension: 
[x.capitalize() for x in ['cat', 'dog', 'cow']]

# Filter
even = lambda x: x % 2 == 0
list(filter(even, range(11)))
# using list comprehension: 
[x for x in range(11) if x % 2 == 0]

# Reduce
import functools
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
functools.reduce(lambda acc, pair: acc+ pair[0], pairs, 0)
# using generator expression
sum(x[0] for x in pairs)
