def decorator(func):
    def wrapper(name):
        if name == "Shubham":
            print(f"Hello, {name}!")
        func(name)
    return wrapper


@decorator
def wish(data):
    print(f"Welcome to the application: {data}")


res = input("Enter your name:")
wish(res)

decorfunc = decorator(wish)
decorfunc(res)