#!/usr/bin/env python3

def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def main() -> None:
    first_number: float = get_number("Enter the first number: ")
    second_number: float = get_number("Enter the second number: ")
    total: float = first_number + second_number
    print(f"Sum: {total}")


if __name__ == "__main__":
    main()

