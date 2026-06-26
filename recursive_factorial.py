"""
Project: Recursive Factorial Calculator
Author: Naman Sharma

This program calculates the factorial of a number
using recursion.
"""

def factorial(number):
    """
    Calculates factorial using recursion.

    Parameters:
        number (int): A non-negative integer.

    Returns:
        int: Factorial of the number.
    """

    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


def main():

    print("=" * 45)
    print("      Recursive Factorial Calculator")
    print("=" * 45)

    try:

        number = int(input("Enter a non-negative integer: "))

        answer = factorial(number)

        print("\nResult")
        print("-" * 45)
        print(f"Factorial of {number} = {answer}")

    except ValueError as error:
        print("\nError:", error)


if __name__ == "__main__":
    main()