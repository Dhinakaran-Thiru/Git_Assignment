def is_perfect_square(n):
    # If the square root of the number is an integer, it's a perfect square
    return int(n ** 0.5) ** 2 == n

# Example usage:
num1 = 25
num2 = 30

print(is_perfect_square(num1))  # Output: True (25 is a perfect square)
print(is_perfect_square(num2))  # Output: False (30 is not a perfect square)
print("something but do nothing")