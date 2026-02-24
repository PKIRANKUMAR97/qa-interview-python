def decorator(func):
    def wrapper():
        print("Before calling the oruginal function")
        func()
        print("After calling the oruginal function")
    return wrapper

@decorator
def meow():
    print("Hello world this is cat bro")

meow()