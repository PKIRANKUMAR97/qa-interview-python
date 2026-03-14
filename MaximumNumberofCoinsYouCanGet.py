l = int(input())

list1=[int(input()) for i in range(l)]


def fun(ls):
    rev_ele = ""
    if ls[0] == 'apple':
        for char in ls[1]:
            rev_ele = char + rev_ele
        ls.pop(1)
        ls.append(rev_ele)
    return ls


print(fun(["apple", "orange"]))




