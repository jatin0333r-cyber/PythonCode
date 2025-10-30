def main():
    s = input("Enter an integer: ")
    try:
        n = int(s)
    except ValueError:
        print("Not an integer")
    else:
        print("Converted:", n)
    finally:
        print("Cleanup")


if __name__ == "__main__":
    main()

