from datetime import date


def main():
    y1, m1, d1 = map(int, input("Birth (YYYY MM DD): ").split())
    y2, m2, d2 = map(int, input("Target (YYYY MM DD): ").split())
    birth = date(y1, m1, d1)
    target = date(y2, m2, d2)
    years = target.year - birth.year
    if (target.month, target.day) < (birth.month, birth.day):
        years -= 1
    print("Age:", years)


if __name__ == "__main__":
    main()

