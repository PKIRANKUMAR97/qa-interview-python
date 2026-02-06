# The Vowel Counter:
# Write a program that takes a string and counts how many vowels (a, e, i, o, u)
# it contains using a for loop.

str1=input("Enter a string : ")

def vowelCounter(str1):
    count_vowels = 0
    for i in str1:
        if i in "aeiou":
            count_vowels=count_vowels+1
    return count_vowels

print(vowelCounter(str1))