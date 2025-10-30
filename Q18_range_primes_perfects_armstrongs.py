def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n):
    if n <= 1:
        return False
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n


def is_armstrong(n):
    s = str(abs(n))
    p = len(s)
    total = 0
    for ch in s:
        total += int(ch) ** p
    return total == abs(n)


def main():
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))
    primes = []
    perfects = []
    armstrongs = []

    for n in range(start, end + 1):
        if is_prime(n):
            primes.append(n)
        if is_perfect(n):
            perfects.append(n)
        if is_armstrong(n):
            armstrongs.append(n)

    print("Primes:", primes)
    print("Perfects:", perfects)
    print("Armstrongs:", armstrongs)


if __name__ == "__main__":
    main()

