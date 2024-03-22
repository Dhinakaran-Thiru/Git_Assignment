def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the string with its reverse
    return s == s[::-1]
 
# Example usage:
string1 = "A man, a plan, a canal, Panama!"
string2 = "racecar"
string3 = "hello"

print(is_palindrome(string1))  # Output: True
print(is_palindrome(string2))  # Output: True
print(is_palindrome(string3))  # Output: False
i edited in that file using main branch
