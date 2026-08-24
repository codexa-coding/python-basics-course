"""
Lesson 1: Variables and basic data types.

A variable is a named reference to a value.
Python determines the type automatically based on the assigned value.
"""


def calculate_total(price: float, quantity: int) -> float:
    """Return the total cost for a product order."""
    return price * quantity


def format_user_message(name: str, age: int) -> str:
    """Create a readable message using an f-string."""
    return f"{name} is {age} years old."


def main() -> None:
    # Strings store text.
    company_name = "Codexa"

    # Integers are whole numbers.
    employee_count = 12

    # Floats are decimal numbers.
    monthly_cost = 49.99

    # Booleans are either True or False.
    is_active = True

    print("=== Variables and Types ===")
    print(company_name)
    print(employee_count)
    print(monthly_cost)
    print(is_active)

    print("\n=== Checking Types ===")
    print(type(company_name))
    print(type(employee_count))
    print(type(monthly_cost))
    print(type(is_active))

    print("\n=== Arithmetic ===")
    subtotal = calculate_total(price=19.99, quantity=3)
    print(f"Subtotal: ${subtotal:.2f}")

    print("\n=== Type Conversion ===")
    number_as_text = "42"
    converted_number = int(number_as_text)
    print(converted_number + 8)

    print("\n=== String Formatting ===")
    print(format_user_message("Alex", 28))


if __name__ == "__main__":
    main()
