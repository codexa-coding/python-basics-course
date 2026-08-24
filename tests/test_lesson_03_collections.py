import pytest

from python_basics.lesson_03_collections import average, count_words, unique_tags


def test_average() -> None:
    assert average([2.0, 4.0, 6.0]) == 4.0


def test_average_rejects_empty_list() -> None:
    with pytest.raises(ValueError):
        average([])


def test_count_words() -> None:
    result = count_words("Python is useful. Python is readable!")
    assert result == {
        "python": 2,
        "is": 2,
        "useful": 1,
        "readable": 1,
    }


def test_unique_tags() -> None:
    assert unique_tags(["python", "python", "testing"]) == {"python", "testing"}
