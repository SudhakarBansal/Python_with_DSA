# GCD of Two Numbers

# Input: n = 56, m = 98
# Output: 14

def gcd(n, m):
    """
    Function to find the GCD of two integers without using built-in functions and recursion.
    
    Parameters:
    n (int): The first integer.
    m (int): The second integer.
    
    Returns:
    int: The GCD of n and m.
    """
    # Your code here
    # result = 1
    # min_number,max_number = min(m,n),max(m,n)
    # if max_number%min_number==0:
    #     return min_number
    # for i in range(1,min_number//2):
    #     if m%i ==0 and n%i ==0:
    #         result = i
    # return result



    # following is the better approach using Euclidean algorithm iteratively

    while m!=0:
        m,n = n%m,m
    return n


print(gcd(24,18))