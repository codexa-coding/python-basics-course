import pytest

from python_basics.lesson_02_control_flow import countdown, find_even_numbers, get_grade


@pytest.mark.parametrize(
    ("score", "expected_grade"),
    [
        (100, "A"),
        (90, "A"),
        (89, "B"),
        (70, "C"),
        (60, "D"),
        (59, "F"),
    ],
)
def test_get_grade(score: int, expected_grade: str) -> None:
    assert get_grade(score) == expected_grade


def test_get_grade_rejects_invalid_score() -> None:
    with pytest.raises(ValueError):
        get_grade(101)


def test_find_even_numbers() -> None:
    assert find_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_countdown() -> None:
    assert countdown(3) == [3, 2, 1]
