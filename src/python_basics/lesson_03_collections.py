"""
Lesson 3: Collections.

Collections hold multiple values.

- list: ordered and mutable
- tuple: ordered and immutable
- dictionary: key-value pairs
- set: unique values
"""


def average(numbers: list[float]) -> float:
    """Return the arithmetic mean of a non-empty list."""
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")

    return sum(numbers) / len(numbers)


def count_words(text: str) -> dict[str, int]:
    """Count each lowercase word in a string."""
    counts: dict[str, int] = {}

    for word in text.lower().split():
        cleaned_word = word.strip(".,!?;:")
        counts[cleaned_word] = counts.get(cleaned_word, 0) + 1

    return counts


def unique_tags(tags: list[str]) -> set[str]:
    """Return the unique values from a tag list."""
    return set(tags)


def main() -> None:
    print("=== Lists ===")
    languages = ["Python", "JavaScript", "Go"]
    languages.append("Rust")
    print(languages)
    print(languages[0])
    print(languages[-1])

    print("\n=== Tuples ===")
    coordinates = (51.5072, -0.1276)
    print(f"Latitude: {coordinates[0]}, longitude: {coordinates[1]}")

    print("\n=== Dictionaries ===")
    developer = {
        "name": "Maya",
        "role": "Backend Engineer",
        "experience_years": 4,
    }
    developer["location"] = "Remote"

    for key, value in developer.items():
        print(f"{key}: {value}")

    print("\n=== Sets ===")
    tags = ["python", "api", "python", "testing", "api"]
    print(unique_tags(tags))

    print("\n=== Aggregation ===")
    scores = [80.0, 92.5, 76.0, 88.5]
    print(f"Average score: {average(scores):.2f}")

    print("\n=== Word Counter ===")
    print(count_words("Python is useful. Python is readable!"))


if __name__ == "__main__":
    main()
