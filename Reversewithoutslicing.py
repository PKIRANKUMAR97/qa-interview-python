def fun_revstringwithoutslicing(s):
    rev_s =""
    for char in s:
        rev_s=char + rev_s

    return rev_s

print(fun_revstringwithoutslicing("solutions"))