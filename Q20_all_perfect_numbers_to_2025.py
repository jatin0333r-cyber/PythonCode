def is_perfect(n):
    if n <= 1:
        return False
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n


def main():
    perfects = []
    for n in range(1, 2026):
        if is_perfect(n):
            perfects.append(n)
    print("Perfect numbers from 1 to 2025:")
    print(perfects)
    print("Total count:", len(perfects))


if __name__ == "__main__":
    main()

