l1=[91,2756,33,49,52,78,90,334,234,897,33,6,333]
large=l1[0]

for i in range (0,len(l1)):
    if l1[i] > large:
        large=l1[i]
print(large)
