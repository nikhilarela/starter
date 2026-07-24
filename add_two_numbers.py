#!/usr/bin/env python3

from typing import Final


def read_number(prompt: str) -> float:
    """Prompt the user for a number until a valid numeric value is entered."""
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    first_number = read_number("Enter the first number: ")
    second_number = read_number("Enter the second number: ")
    result: Final[float] = first_number + second_number
    print(f"The sum is: {result}")


if __name__ == "__main__":
    main()

