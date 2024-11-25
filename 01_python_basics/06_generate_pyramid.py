def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' with n rows as a list of strings,
    including trailing spaces to maintain equal-width formatting.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    pyramid = []
    for i in range(1, n + 1):
        # Number of stars in the current row
        stars = 2 * i - 1
        # Number of spaces before and after stars
        spaces = n - i
        # Construct the row with equal-length formatting
        pyramid.append(" " * spaces + "*" * stars + " " * spaces)
    return pyramid

# Example usage
print(generate_pyramid(3))
