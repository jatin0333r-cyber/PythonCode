def main():
    # Numbers
    integer_val = 10
    float_val = 3.5
    complex_val = 2 + 3j

    # Boolean
    is_active = True

    # String
    greeting = "Hello"

    # List, Tuple, Set, Dict
    fruits = ["apple", "banana", "cherry"]
    coordinates = (10, 20)
    unique_numbers = {1, 2, 3, 2}
    student = {"name": "Alice", "age": 20}

    print(integer_val, type(integer_val))
    print(float_val, type(float_val))
    print(complex_val, type(complex_val))
    print(is_active, type(is_active))
    print(greeting, type(greeting))
    print(fruits, type(fruits))
    print(coordinates, type(coordinates))
    print(unique_numbers, type(unique_numbers))
    print(student, type(student))


if __name__ == "__main__":
    main()

