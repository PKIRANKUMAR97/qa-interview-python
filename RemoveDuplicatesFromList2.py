def fun_revstringwith(l):

    for i in l:
        if l.count(i)>1:
            l.pop(i)

    return l

print(fun_revstringwith([1,2,3,2,3]))

