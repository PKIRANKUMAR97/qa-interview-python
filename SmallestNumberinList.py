l1=[91,27,33,49,52,78,90,334,234,897,3344,6]
small=l1[0]

for i in range(1,len(l1)):
    if l1[i] < small:
        small=l1[i]
print(small)