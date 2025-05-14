# Function to calculate factorial using a loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Sample call
number = int(input("Enter a number to calculate factorial:  "))
print(f"The factorial of {number} is: {factorial(number)}")
