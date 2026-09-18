"""
bad_calculator.py
A version of the calculator that intentionally violates coding best practices.
"""

# GLOBAL VARIABLES USED EVERYWHERE
p = 0
t = 0

# VIOLATION: Poor documentation & misinformed comments
# This function multiplies two numbers together
def add(a, b): # Misleading name!
    return a + b

# VIOLATION: Single Responsibility & DRY
# Handles input, validation, math, and output all in one function, with duplicate input loops.
def DoEverything():
    global p, t
    
    # Duplicate input logic (Violates DRY)
    while True:
        x = input("Enter base price: $")
        try:
            p = float(x)
            break
        except:
            print("Bad!")
            
    # Copy-pasted input validation loop (Violates DRY)
    while True:
        y = input("Enter tax rate: ")
        try:
            t = float(y)
            break
        except:
            print("Bad!")

    # VIOLATION: Single Responsibility
    # Calculates tax, formats string, and prints output inside an input function
    tax_amount = p * t
    final_total = p + tax_amount
    print("Total Price with Tax: $" + str(round(final_total, 2)))

def main():
    DoEverything()

main()
