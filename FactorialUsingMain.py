def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        i=i+1
    print(fact)

def main():
    n=int(input("Enter the number to find factorial:"))
    factorial(n)

if __name__=="__main__":
    main()