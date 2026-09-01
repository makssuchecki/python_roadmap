# Treats program computation as the evaluation of mathematical functions based on lambda calculus.

sample_characters = ['p','y','t','h','o','n']
import functools
sample_string = functools.reduce(lambda s, c: s + c, sample_characters)
print(sample_string)