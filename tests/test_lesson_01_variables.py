from python_basics.lesson_01_variables import calculate_total, format_user_message


def test_calculate_total() -> None:
    assert calculate_total(12.50, 4) == 50.0


def test_format_user_message() -> None:
    assert format_user_message("Taylor", 30) == "Taylor is 30 years old."
