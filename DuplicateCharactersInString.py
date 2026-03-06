def func_duplicatecharactersinstring(s):
    duplicates = []
    for char in s:
        if s.count(char) > 1 and char not in duplicates:
            duplicates.append(char)
    print(duplicates)
    return len(duplicates)

print(func_duplicatecharactersinstring("qerwcrfcdcwerfwfasadqwe"))