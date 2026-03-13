def fun_revstringwith(l):
    dup=[]
    for i in l:
        if i not in dup and l.count(i)>1:
            dup.append(i)

    return dup

print(fun_revstringwith([1,2,3,2,3]))

