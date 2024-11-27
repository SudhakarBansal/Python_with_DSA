# Reverse a string

# Input: "hello"
# Output: "olleh"
 
# Input: "Python"
# Output: "nohtyP"

def reverse_string(s):
    """
    Function to return the reversed version of the input string.
    
    Parameters:
    s (str): The input string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    # Your code here
    l = len(s) -1
    result_string=""
    for i in range(l,-1,-1):
        result_string+=s[i]
    return result_string

print(reverse_string("hello"))