def main():
    n = int(input("Enter number: "))
    if n <= 1:
        print("Not Prime")
        return
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            return
    print("Prime")


if __name__ == "__main__":
    main()

