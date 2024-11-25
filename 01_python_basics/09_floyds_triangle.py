# Floyds Triangle

# Input: 5
# Output: ['1', '2 3', '4 5 6', '7 8 9 10', '11 12 13 14 15']

def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    # Your code here
    
    floyds_triangle = []
    num = 1
    for i in range(1, n + 1):
        row = " ".join(str(num + j) for j in range(i))
        floyds_triangle.append(row)
        num += i
    return floyds_triangle

print(generate_floyds_triangle(5))
