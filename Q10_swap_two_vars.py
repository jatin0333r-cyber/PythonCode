def main():
    a, b = 10, 20
    print("Original:", a, b)
    # Pythonic swap
    a, b = b, a
    print("Pythonic:", a, b)
    # Temp variable
    a, b = 10, 20
    temp = a
    a = b
    b = temp
    print("Temp:", a, b)


if __name__ == "__main__":
    main()

