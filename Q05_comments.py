def main():
    # This is a single-line comment
    x = 5  # Inline comment next to code

    """
    This is a multi-line string that can be used as a block comment
    for documentation or explanation within the code.
    """

    print("Single-line and inline comments demonstrated. x =", x)

    # Docstring example using a function
    def add(a, b):
        """Return the sum of a and b."""
        return a + b

    print("Docstring of add():", add.__doc__)


if __name__ == "__main__":
    main()

