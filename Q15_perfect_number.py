def main():
    n = int(input("Enter number: "))
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s == n and n != 0:
        print("Perfect")
    else:
        print("Not Perfect")


if __name__ == "__main__":
    main()

