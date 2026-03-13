str1 = input("Enter the string : ")
str_rev =""

for char in str1:
    str_rev = char + str_rev

print(str_rev)
if str1 == str_rev :
    print("String is palindrome")
else :
    print("String is not palindrome")