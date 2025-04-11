
class Currency:
    def __init__(self, symbol: str, name: str):
        self.symbol = symbol
        self.name = name

    def get_symbol(self):
        return self.symbol


class Price:
    def __init__(self, amount: float, currency: Currency):
        self.amount = amount
        self.currency = currency

    def apply_discount(self, discount_rate: float):
        if not isinstance(discount_rate, (int, float)):
            raise ValueError("Discount rate must be a number")
        if discount_rate < 0 or discount_rate > 100:
            raise ValueError("Discount rate must be between 0 and 100")
        return self.amount - ((discount_rate / 100) * self.amount)

    def get_discounted_price(self, discount_rate: float):
        discounted = self.apply_discount(discount_rate)
        return f"{self.currency.get_symbol()}{discounted:.2f}"
