def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def calculate_shipping_cost(
    order_total: float,
    country: str,
    is_expedited: bool = False,
) -> float:
    normalized_country = country.strip().lower()
    is_domestic = normalized_country in {"us", "usa", "united states"}

    if order_total >= 100:
        standard_shipping = 0.0
    elif is_domestic:
        standard_shipping = 5.0
    else:
        standard_shipping = 15.0

    expedited_fee = 10.0 if is_expedited else 0.0
    return standard_shipping + expedited_fee


def summarize_scores(scores: list[float]) -> dict[str, float]:
    if not scores:
        raise ValueError("Scores cannot be empty.")

    return {
        "min": min(scores),
        "max": max(scores),
        "average": sum(scores) / len(scores),
    }
