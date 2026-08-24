from pathlib import Path


def count_lines(file_path: Path) -> int:
    with file_path.open("r", encoding="utf-8") as file:
        return sum(1 for _ in file)


def parse_integer(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None
