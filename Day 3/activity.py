#Activity: Create a base calculator with input value.

# Base Calculator
# User input
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %): ")
num2 = float(input("Enter second number: "))

# Logic for calculation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
elif operator == "%":
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

# Output
print("Result:", result)
