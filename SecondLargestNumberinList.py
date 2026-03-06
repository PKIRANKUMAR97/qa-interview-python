def func_SecondLargestNumberinList(list1):
    for i in range(0, len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]

    return list1[1]

print(int)

list1 = [23, 45, 12, 23, 45, 34, 13]
print(func_SecondLargestNumberinList(list1))

"""
nums = [10, 20, 4, 45, 99]

nums.sort()

print(nums[-2])
"""