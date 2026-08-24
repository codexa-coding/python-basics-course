"""
Lesson 2: Control flow.

Control flow determines which code runs and how often it runs.
This includes conditionals and loops.
"""


def get_grade(score: int) -> str:
    """Convert a numeric score from 0 to 100 into a letter grade."""
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def find_even_numbers(numbers: list[int]) -> list[int]:
    """Return only the even numbers from a list."""
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


def countdown(start: int) -> list[int]:
    """Return a countdown list from start down to 1."""
    result = []

    while start > 0:
        result.append(start)
        start -= 1

    return result


def main() -> None:
    print("=== Conditionals ===")
    score = 84
    print(f"Score: {score}, grade: {get_grade(score)}")

    print("\n=== For Loops ===")
    names = ["Ada", "Grace", "Linus"]

    for name in names:
        print(f"Hello, {name}!")

    print("\n=== Range ===")
    for number in range(1, 6):
        print(number)

    print("\n=== Filtering Values ===")
    values = [3, 4, 7, 8, 10, 13]
    print(find_even_numbers(values))

    print("\n=== While Loops ===")
    print(countdown(5))


if __name__ == "__main__":
    main()
