# Check if a number is Armstrong number
original_num=int(input("Enter a number: "))
def Armstrong(original_num):
    digits = [int(d) for d in str(original_num)]
    length_of_number=len(str(original_num))
    sum=0
    for i in range(len(digits)):
        sum = sum + (digits[i] ** length_of_number)

    return sum

if original_num == Armstrong(original_num):
        print("Armstrong number only..")
else:
        print("Not Armstrong number only..")



