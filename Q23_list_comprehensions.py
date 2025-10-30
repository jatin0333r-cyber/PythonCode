def main():
    nums = list(range(1, 6))
    squares = [n * n for n in nums]
    evens = [n for n in nums if n % 2 == 0]
    pairs = [(i, j) for i in range(1, 3) for j in range(1, 3)]

    print(nums)
    print(squares)
    print(evens)
    print(pairs)


if __name__ == "__main__":
    main()

