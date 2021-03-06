"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while numerator == 0 or denominator == 0:
        print("Cannot divide by zero!")
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

# 1. A ValueError will occur when either inputs are not valid
#    (ie. the input not being a number)
# 2. A ZeroDivisionError will occur when at least one input is equal to zero
# 3. Yes (shown above)
