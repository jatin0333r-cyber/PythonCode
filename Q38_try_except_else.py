def main():
    s = input("Enter an integer: ")
    try:
        n = int(s)
    except ValueError:
        print("Not an integer")
    else:
        print("Success:", n)


if __name__ == "__main__":
    main()

