# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#     return wrapper


# @decorator
# def say_hello(name):
#     print(f"Hello, {name}!")

# say_hello("Alice")

def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper


@decorator
def my_function():
    print("Hello, World!")

my_function()
