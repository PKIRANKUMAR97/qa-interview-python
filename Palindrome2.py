num = int(input("Enter a number: "))
org = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10


if reverse == org :
    print("The number is palindrome")
else:
    print("The number is not palindrome")