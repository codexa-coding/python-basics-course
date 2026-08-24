from python_basics.lesson_04_functions import (
    calculate_invoice_total,
    greet,
    is_password_valid,
)


def test_greet_with_default_greeting() -> None:
    assert greet("Alex") == "Hello, Alex!"


def test_greet_with_custom_greeting() -> None:
    assert greet("Alex", "Welcome") == "Welcome, Alex!"


def test_password_validation() -> None:
    assert is_password_valid("SecurePass7") is True
    assert is_password_valid("weakpass") is False
    assert is_password_valid("NO_DIGITS_HERE") is False


def test_calculate_invoice_total() -> None:
    total = calculate_invoice_total([10.0, 20.0], tax_rate=0.10, discount=5.0)
    assert total == 27.5
