def fun(*args):
    return sum(args)

print(fun(1, 2, 3))


def func1(*arg):
    for i in arg:
        print(i)


func1(1, 2, 3, 4, 5)