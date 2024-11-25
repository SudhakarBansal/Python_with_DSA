# Hollow Square of side 'N'

def generate_hollow_square(n:int)->list[str]:
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    hollow_square=[]
    for i in range(n):
        if i==0 or i==n-1:
            hollow_square.append(n*"*")
        else:
            hollow_square.append("*"+ ((n-2)*" ")+"*")
    return hollow_square
    
print(generate_hollow_square(3))