"""
currency_converter.py

A simple CLI tool to convert INR to USD, EUR, or JPY.
Includes input validation, currency symbols, and repeat option.
"""


def currency_converter():
    """
    Converts INR to selected foreign currency using predefined rates.
    Handles invalid inputs and allows repeated conversions.
    """
    rates = {
        "USD": 0.012,
        "EUR": 0.011,
        "JPY": 1.75
    }

    print("-" * 40)
    print("   💱 Welcome to currency calculator!")
    print("-" * 40)
    while True:
        while True:
            try:
                amount = int(input("Enter the ₹ INR: "))
                break
            except ValueError:
                print("Invalid input... Enter in numbers")

        currency = input("Convert to which currency? (USD/EUR/JPY): ").upper()

        if currency in rates:
            converted = amount * rates[currency]
            if currency == "USD":
                print(f"Converted amount is : {converted} $")
            elif currency == "EUR":
                print(f"Converted amount is : {converted} €")
            elif currency == "JPY":
                print(f"Converted amount is : {converted} ¥")
        else:
            print("Invalid currency choice. Please choose USD, EUR, or JPY.")

        while True:
            again = input("Wanna convert again y/n : ").lower()
            if again in ["no", "n", "yes", "y"]:
                break
            print("Invalid choice... Choose y/n ")

        if again in ["n", "no"]:
            print("-" * 40)
            print("             👋 Goodbye!")
            print("-" * 40)
            break
        print("-" * 40)
        print("\n")

if __name__ == "__main__":
    currency_converter()
