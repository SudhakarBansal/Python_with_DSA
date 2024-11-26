# Valid Perfect Square

def is_perfect_square(num):
    """
    Function to check if a number is a perfect square.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if num is a perfect square, False otherwise.
    """
    # Your code here
    if num<1:
        return False

    i=1
    while(i*i <= num):
        if i*i==num:
            return True
        i+=1
    return False

print(is_perfect_square(2))