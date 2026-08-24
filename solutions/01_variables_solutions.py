def convert_minutes_to_seconds(minutes: int) -> int:
    return minutes * 60


def full_name(first_name: str, last_name: str) -> str:
    return f"{first_name.strip().title()} {last_name.strip().title()}"


def calculate_percentage(part: float, total: float) -> float:
    if total == 0:
        raise ValueError("Total cannot be zero.")

    return (part / total) * 100
