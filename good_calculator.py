"""
good_calculator.py
A clean, modular command-line calculator demonstrating best coding practices.
"""

def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b

def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b

def apply_tax(amount: float, tax_rate: float = 0.07) -> float:
    """Calculate total cost after applying a percentage tax rate."""
    return amount + multiply(amount, tax_rate)

def get_valid_number(prompt: str) -> float:
    """Repeatedly prompt the user until a valid floating-point number is provided."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def main():
    """Main execution loop for the calculator program."""
    print("=== Clean Calculator ===")
    price = get_valid_number("Enter base price: $")
    tax_rate = get_valid_number("Enter tax rate (e.g., 0.07 for 7%): ")
    
    total = apply_tax(price, tax_rate)
    print(f"Total Price with Tax: ${total:.2f}")

if __name__ == "__main__":
    main()
