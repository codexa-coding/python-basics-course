def is_leap_year(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def fizz_buzz(limit: int) -> list[str]:
    results = []

    for number in range(1, limit + 1):
        if number % 15 == 0:
            results.append("FizzBuzz")
        elif number % 3 == 0:
            results.append("Fizz")
        elif number % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(number))

    return results


def count_positive_numbers(numbers: list[int]) -> int:
    count = 0

    for number in numbers:
        if number > 0:
            count += 1

    return count
