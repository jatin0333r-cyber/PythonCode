def main():
    parts = input("Enter values (commas): ").split(",")
    parts = [p.strip() for p in parts]
    print(", ".join(parts))


if __name__ == "__main__":
    main()

