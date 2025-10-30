def main():
    n = int(input("Enter number: "))
    s = str(abs(n))
    p = len(s)
    total = 0
    for ch in s:
        total += int(ch) ** p
    if total == abs(n):
        print("Armstrong")
    else:
        print("Not Armstrong")


if __name__ == "__main__":
    main()

