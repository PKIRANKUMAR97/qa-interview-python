l = [32, 546, 324, 57, 46, 88]

def  ascending_order(l):
    for i in range(len(l)):
        for j in range(i+1 ,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]

    return l

print(ascending_order(l))