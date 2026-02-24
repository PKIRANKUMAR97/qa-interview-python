n = int(input("enter a number n : "))

def is_prime(n):
    if n<=1:
        return False

    for i in range(2,n):
        if n% i ==0:
            return False


    return True

if is_prime(n):
    print(n," is prime")
else:
    print(n," is not prime")
