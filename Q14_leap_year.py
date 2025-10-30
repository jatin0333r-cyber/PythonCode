def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def main() -> None:
    year_str = input("Enter year: ")
    try:
        year = int(year_str)
    except ValueError:
        print("Invalid year")
        return
    print("Leap Year" if is_leap_year(year) else "Not a Leap Year")


if __name__ == "__main__":
    main()

