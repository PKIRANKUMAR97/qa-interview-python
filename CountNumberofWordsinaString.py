str1 = input(" enter string : ")

def func_CountNumberofWordsinaString(str1):
    str2=str1.split(" ")

    return len(str2)

print(func_CountNumberofWordsinaString(str1))