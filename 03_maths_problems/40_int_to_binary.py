# Decimal to Binary

# Input: n = 5
# Output: "101"

def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    # Your code here
    binary_val = ""
    is_negative = n < 0
    n = abs(n)

    if n == 0:
        return "0"  # Special case for zero

    while n>0:
        if n % 2 ==0:
            binary_val=binary_val+"0"
        else :
            binary_val = binary_val+"1"
        n = n//2
        
    if is_negative:
        binary_val = binary_val+"-"

    binary_val = ''.join(reversed(binary_val))

    return binary_val

print(int_to_binary(-4))