def is_prime(n):
    """
    Function to check if a number is prime without using built-in functions.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, False if n is not.
    """
    # Handle special cases
    if n <= 1:
        return False
    if n == 2:  # 2 is a prime number
        return True
    if n % 2 == 0:  # Any even number greater than 2 is not prime
        return False
    
    # Check divisibility for odd numbers from 3 up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2  # Skip even numbers
    
    return True

print(is_prime(7))