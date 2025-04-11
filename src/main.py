
from app import Currency, Price

def main():
    try:
        price_input = float(input("Enter the price (e.g. 100): "))
        discount_input = float(input("Enter the discount rate (e.g. 20 for 20%): "))
        
        currency = Currency("€", "Euro")
        price = Price(price_input, currency)
        result = price.get_discounted_price(discount_input)
        
        print(f"Discounted price: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
