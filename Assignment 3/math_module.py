## Math Module for Calculations
import math

# Ask the user for a number
num = float(input("Enter a number: "))

# Calculate required values using math module
square_root = math.sqrt(num)
natural_log = math.log(num)        # log base e
sine_value = math.sin(num)         # in radians

# Display results
print(f"Square root of {num} = {square_root}")
print(f"Natural logarithm of {num} = {natural_log}")
print(f"Sine of {num} radians = {sine_value}")
