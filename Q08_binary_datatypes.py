def main():
    # bytes (immutable)
    b = bytes([65, 66, 67])  # A, B, C
    print(b)

    # bytearray (mutable)
    ba = bytearray([68, 69, 70])  # D, E, F
    ba[0] = 71  # change D to G
    print(ba)


if __name__ == "__main__":
    main()

