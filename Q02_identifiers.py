def demonstrate_valid_identifiers():
    student_name = "Alice"
    age2 = 20
    _private_value = 42
    UPPER_CASE = True
    camelCase = 3.14
    print("Valid identifiers and their values:")
    print("student_name:", student_name)
    print("age2:", age2)
    print("_private_value:", _private_value)
    print("UPPER_CASE:", UPPER_CASE)
    print("camelCase:", camelCase)

def demonstrate_invalid_identifiers():
    print("\nAttempting invalid identifiers (caught as SyntaxError):")
    invalid_snippets = [
        "2age = 10",            # starts with digit
        "student-name = 'Bob'", # hyphen not allowed
        "class = 5",            # keyword not allowed
        "first name = 'Eve'",   # space not allowed
    ]
    for code in invalid_snippets:
        try:
            exec(code, {})
        except SyntaxError as exc:
            print(f"Invalid: {code!r} -> SyntaxError: {exc.msg}")
        except Exception as exc:  # Fallback in case other errors occur
            print(f"Invalid: {code!r} -> Error: {exc}")


def main():
    demonstrate_valid_identifiers()
    demonstrate_invalid_identifiers()


if __name__ == "__main__":
    main()

