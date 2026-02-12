def has_numbers(string1):
    for char in string1:
        if char.isdigit():
            return True
    return False

def main():
    string1=input("Enter a string: ")
    print(has_numbers(string1))

if __name__=="__main__":
    main()
