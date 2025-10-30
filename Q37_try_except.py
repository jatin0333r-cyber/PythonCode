def main():
    s = input("Enter an integer: ")
    try:
        n = int(s)
        print("You entered:", n)
    except ValueError:
        print("Not an integer")


if __name__ == "__main__":
    main()

