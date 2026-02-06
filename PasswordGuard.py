# The Password Guard: Write a program that keeps asking a user to input a password.
# The loop should only exit when the user types "Python123".
def PG():
    while True:
        enter_pwd = input("Enter password: ")
        if enter_pwd == "Python123":
            print("Access Granted ✅")
            break
        else:
            print("Wrong password ❌ Try again")

PG()

