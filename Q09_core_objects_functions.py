def main():
    nums = [1, 2, 3, 4]
    print(len(nums))
    print(sum(nums))
    print(min(nums), max(nums))
    print(all([True, True]), any([False, True]))
    for i, v in enumerate(nums):
        print(i, v)


if __name__ == "__main__":
    main()

