# Write python code to demostrate the use of decorator

# A simple decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Function to be decorated
def say_hello():
    print("Hello!")

# Decorating the function
say_hello = my_decorator(say_hello)

# Calling the decorated function
say_hello()

print("\n" + "="*50 + "\n")

# Using the @ syntax for decorator
@my_decorator
def say_goodbye():
    print("Goodbye!")

# Calling the decorated function
say_goodbye()