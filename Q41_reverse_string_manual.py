# Q41: WAP in Python to reverse a string without using predefined functions

# Simple method to reverse a string manually
def reverse_string(text):
    # Create an empty string to store the reversed result
    reversed_text = ""
    
    # Go through each character from the end to the beginning
    for i in range(len(text) - 1, -1, -1):
        reversed_text = reversed_text + text[i]
    
    return reversed_text

# Main program
print("String Reversal Program")
print("-" * 25)

# Get input from user
user_string = input("Enter a string: ")

# Reverse the string
reversed_result = reverse_string(user_string)

# Display results
print(f"Original: {user_string}")
print(f"Reversed: {reversed_result}")

# Show how it works step by step
print("\nStep by step process:")
for i in range(len(user_string)):
    char_position = len(user_string) - 1 - i
    print(f"Step {i+1}: Take character '{user_string[char_position]}' from position {char_position}")