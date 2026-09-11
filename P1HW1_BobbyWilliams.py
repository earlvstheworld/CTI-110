# Bobby Williams
# 09/10/2026    
# Calculating exponents and addition and subtraction

# Calculate exponents
print("------Exponents-------")
print()

base = int(input("Enter a base number: "))
exponent = int(input("Enter a exponent: "))
result = base ** exponent
print(base, "raised to the power of", exponent, "is", result, "!!")

# Calculate addition and subtraction
print("------Addition and Subtraction-------")
print()

num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter a integer to add: "))
num3 = int(input("Enter a integer to subtract: "))

sum_result = num1 + num2
final_result = sum_result - num3
print(num1, "plus", num2, "minus", num3, "is equal to", final_result, "!!")