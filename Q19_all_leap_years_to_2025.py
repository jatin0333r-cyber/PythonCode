def is_leap_year(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


def main():
    years = []
    for y in range(1, 2026):
        if is_leap_year(y):
            years.append(y)
    print("Leap years from 1 to 2025:")
    print(years)
    print("Total count:", len(years))


if __name__ == "__main__":
    main()

