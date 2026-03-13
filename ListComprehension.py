"""
syntax :

[expression for item in iterable if condition ]


"""

# find common elements in two lists

a = [1,2,3,4]
b = [3,4,5,6]

c=[x for x in a if x in b]
print(c)
