def main():
    s = input("Enter an integer: ")
    try:
        n = int(s)
        print("Parsed:", n)
    except ValueError:
        print("Not an integer")
    finally:
        print("Always runs (finally)")


if __name__ == "__main__":
    main()

