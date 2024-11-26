# Hollow Inverted Right Triangle

# Input: 4
# Output: ['****', '* *', '**', '*']
 
def generate_hollow_inverted_right_angled_triangle(n):
    """
    Function to return a hollow inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    
    hollow_inverted_right_angled_triangle=[]
    for i in range(n,0,-1):
        if i==1 or i==n:
            hollow_inverted_right_angled_triangle.append(i*"*")
        else:
            hollow_inverted_right_angled_triangle.append("*"+(i-2)*" "+"*")
    return hollow_inverted_right_angled_triangle

print(generate_hollow_inverted_right_angled_triangle(7))