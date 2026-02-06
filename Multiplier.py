# The Multiplier:
# Use range() to print the multiplication table for a number (e.g., 7) from 1 to 10.

x=int(input("Enter the no."))
y=int(input("Enter the no. up to which u need table : "))

def multiply(x,y):
    for i in range(1,y+1):
        print(f"{x} * {i} = {x*i}")

multiply(x,y)