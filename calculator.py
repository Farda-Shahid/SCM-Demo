"""Discount calculation utilities."""


def calculate_discount(price, customer_type):
    """Return the discounted price based on customer type."""
    if customer_type == "premium":
        return price * 0.30
    if customer_type == "member":
        return price * 0.20
    return price * 0.10
