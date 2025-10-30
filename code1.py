def main():
    print("Basic Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Transport (Swap two numbers)")
    
    # Get user's choice
    choice = input("Enter your choice (1-5): ")
    
    # Get two numbers from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Perform the selected operation
    if choice == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    
    elif choice == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    
    elif choice == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    
    elif choice == '4':
        if num2 != 0:  # Check to avoid division by zero
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Cannot divide by zero!")
    
    elif choice == '5':
        # Transport/Swap the numbers
        print(f"Before swapping: num1 = {num1}, num2 = {num2}")
        num1, num2 = num2, num1  # Pythonic way to swap
        print(f"After swapping:  num1 = {num1}, num2 = {num2}")
    
    else:
        print("Invalid choice. Please run the program again and select a valid option.")

main()