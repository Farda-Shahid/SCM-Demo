def calculate_discount(price, is_member):

    if is_member == "regular":
        return price * 0.20

    if is_member == "premium":
            return price * 0.30

    return price * 0.10 