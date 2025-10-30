def main():
    a, b, c = 1, 2, 3
    print("Original:", a, b, c)
    # Pythonic rotate
    a, b, c = c, a, b
    print("Pythonic rotate:", a, b, c)
    # With temp (reset then rotate)
    a, b, c = 1, 2, 3
    t = a
    a = b
    b = c
    c = t
    print("Temp rotate:", a, b, c)


if __name__ == "__main__":
    main()

