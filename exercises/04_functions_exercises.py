"""
Exercises: Functions.
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    pass


def calculate_shipping_cost(
    order_total: float,
    country: str,
    is_expedited: bool = False,
) -> float:
    """
    Calculate shipping cost.

    Rules:
    - Domestic shipping costs $5.00.
    - International shipping costs $15.00.
    - Orders of $100.00 or more receive free standard shipping.
    - Expedited shipping adds $10.00.
    """
    pass


def summarize_scores(scores: list[float]) -> dict[str, float]:
    """
    Return a dictionary containing min, max, and average score.

    Raise ValueError if scores is empty.
    """
    pass
