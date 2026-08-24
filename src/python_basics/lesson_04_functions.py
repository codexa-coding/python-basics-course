"""
Lesson 4: Functions.

Functions group reusable logic into named units.
They can accept parameters and return values.
"""


def greet(name: str, greeting: str = "Hello") -> str:
    """Return a greeting with an optional greeting prefix."""
    return f"{greeting}, {name}!"


def is_password_valid(password: str) -> bool:
    """
    Validate a basic password.

    Rules:
    - At least 8 characters
    - At least one digit
    - At least one uppercase character
    """
    has_minimum_length = len(password) >= 8
    has_digit = any(character.isdigit() for character in password)
    has_uppercase = any(character.isupper() for character in password)

    return has_minimum_length and has_digit and has_uppercase


def calculate_invoice_total(
    item_prices: list[float],
    tax_rate: float = 0.0,
    discount: float = 0.0,
) -> float:
    """Calculate a total after applying a flat discount and percentage tax."""
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative.")

    if discount < 0:
        raise ValueError("Discount cannot be negative.")

    subtotal = sum(item_prices)
    discounted_subtotal = max(0.0, subtotal - discount)
    return discounted_subtotal * (1 + tax_rate)


def main() -> None:
    print("=== Basic Function ===")
    print(greet("Sam"))
    print(greet("Sam", greeting="Welcome"))

    print("\n=== Boolean Function ===")
    password = "SecurePass7"
    print(f"Is password valid? {is_password_valid(password)}")

    print("\n=== Function With Multiple Parameters ===")
    prices = [25.00, 10.50, 64.99]
    total = calculate_invoice_total(prices, tax_rate=0.20, discount=5.00)
    print(f"Invoice total: ${total:.2f}")


if __name__ == "__main__":
    main()
