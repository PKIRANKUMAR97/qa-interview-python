def func(list1):
    set1 = set(list1)
    list2=list(set1)
    return list2

list1 = [1,2,3,4,5,6,7,8,9,9,8,7,6]
print(func(list1))