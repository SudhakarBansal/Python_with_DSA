# Inverted Right Angled Triangle

def generate_inverted_triangle(n):
    """
   Function to return an inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here

    inverted_triangle =[]
    while(n>0):
        inverted_triangle.append(n*"*")
        n=n-1
    
    return inverted_triangle

print(generate_inverted_triangle(5))