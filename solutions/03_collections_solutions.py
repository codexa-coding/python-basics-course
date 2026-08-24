def find_largest(numbers: list[int]) -> int:
    if not numbers:
        raise ValueError("List cannot be empty.")

    return max(numbers)


def merge_unique(first: list[str], second: list[str]) -> list[str]:
    merged = []

    for value in first + second:
        if value not in merged:
            merged.append(value)

    return merged


def invert_dictionary(values: dict[str, str]) -> dict[str, str]:
    return {value: key for key, value in values.items()}
