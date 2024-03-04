def reverse_number(num):
    # Convert the number to a string, reverse it, and convert it back to an integer
    reversed_num = int(str(num)[::-1])
    return reversed_num

# Example usage:
num = 12345
reversed_num = reverse_number(num)
print("Original number:", num)
print("Reversed number:", reversed_num)
