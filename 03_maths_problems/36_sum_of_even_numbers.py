# Sum of N Even Natural Numbers

# Input: n = 3
# Output: 12  # (2 + 4 + 6)


def sum_of_even_numbers(n):
    """
    Function to return the sum of the first n even natural numbers.
    
    Parameters:
    n (int): The number of even numbers to sum.
    
    Returns:
    int: The sum of the first n even natural numbers.
    """
    # Your code here
    total_sum = 0
    current_even_number = 2
    for _ in range(n):
        total_sum+=current_even_number
        current_even_number+=2
    return total_sum

print(sum_of_even_numbers(4))