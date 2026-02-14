def login():
    correct_username="admin"
    correct_password="password123"

    attempts = 0
    max_attempts=4

    while attempts<max_attempts:
        username=input("Please enter your username: ")
        password=input("Please enter your password: ")

        if username==correct_username and password==correct_password:
            print("Login Successful")
            return True
        else :
            attempts+=1
            print("invalid credentials")


    print("Account locked after 4 attempts")
    return False

login()