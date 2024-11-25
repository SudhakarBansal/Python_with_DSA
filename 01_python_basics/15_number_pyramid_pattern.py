# Number Pyramid Pattern

# Input: 4
# Output: ['   1   ', '  1 2  ', ' 1 2 3 ', '1 2 3 4']

def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    # Your code here
    number_pyramid=[]
    for i in range(1,n+1):
        spaces = (n-i)
        numbers = ' '.join(str(x) for x in range(1, i + 1))
        number_pyramid.append(spaces*" "+numbers+spaces*" ")
    return number_pyramid
    
print(generate_number_pyramid(3))
