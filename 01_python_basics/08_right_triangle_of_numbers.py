# Right Angled Triangle with Numbers

# Example:

# Input: 5
# Output: ['1', '22', '333', '4444', '55555']


def generate_number_triangle(n):
    """
    Function to return a right-angled triangle of repeated numbers of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    number_triangle=[i*str(i) for i in range(1,n+1)]

    return number_triangle

print(generate_number_triangle(8))
