list1=[4,45,5567,234,5,239,87,956]

def fun_SortEvenFirstOddLastinList(list1):
    list_even=[]
    list_odd=[]
    for i in range(len(list1)):
        if list1[i] % 2 == 0:
            list_even.append(list1[i])
        else:
            list_odd.append(list1[i])

    total_list=list_even+list_odd
    return total_list
print(fun_SortEvenFirstOddLastinList(list1))
