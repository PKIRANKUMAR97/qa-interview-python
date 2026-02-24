list1 = [1,2,3,4,5,2,3,4]
list2 = []
list3 = []
for item in list1:
    if  item not in list2:
        list2.append(item)
    else:
        list3.append(item)

print(list2)
print(list3)