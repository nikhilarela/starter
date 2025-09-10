#!/usr/bin/env python3

import sys
import argparse


def add_numbers(a: float, b: float) -> float:
    return a + b


def main() -> None:
    parser = argparse.ArgumentParser(description="Add two numbers")
    parser.add_argument("a", nargs="?", type=float, help="First number")
    parser.add_argument("b", nargs="?", type=float, help="Second number")
    args = parser.parse_args()

    if args.a is not None and args.b is not None:
        result = add_numbers(args.a, args.b)
        print(result)
        return

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    print(add_numbers(x, y))


if __name__ == "__main__":
    main()

