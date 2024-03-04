def is_prime(num):
    # Prime numbers are greater than 1
    if num <= 1:
        return False
    
    # Check for factors from 2 to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # Found a factor, not a prime number
    
    return True  # No factors found, it's a prime number

# Example usage:
number = 17

if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
<<<<<<< HEAD
=======
print("commited this 2nd time")
print("commited this 3rd time")
<<<<<<< HEAD
>>>>>>> cb03169 (another last file commited)
=======
>>>>>>> cb03169 (another last file commited)

 3622756 (one file commited)
print("commited this 2nd time")
print("commited this 3rd time")

 newbranch2


 3622756 (one file commited)

3622756 (one file commited)
