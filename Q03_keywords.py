import keyword


def main():
    print("Python keywords:")
    for k in sorted(keyword.kwlist):
        print(k)


if __name__ == "__main__":
    main()

