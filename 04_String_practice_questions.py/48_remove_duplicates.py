#Remove Duplicates in a string

#Input: "programming"
# Output: "progamin"
 
# Input: "Hello, World!"
# Output: "Helo, Wrd!"

def remove_duplicates(s:str)->str:
    """
    Function to remove duplicate characters from the input string.
    
    Parameters:
    s (str): The input string from which duplicates need to be removed.
    
    Returns:
    str: The modified string with duplicates removed.
    """
    # Your code here
    s1 = ""
    seen = set()
    for char in s:
        if not char in seen:
            s1+=char
            seen.add(char)
    return s1

print(remove_duplicates("Hello, World!"))