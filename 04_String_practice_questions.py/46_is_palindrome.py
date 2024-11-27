def is_palindrome(s:str)->bool:
    """
    Function to check if the input string is a palindrome.
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Your code here

    s = ''.join(char.lower() for char in s if char.isalnum())
    start, end = 0, len(s) - 1
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True



print(is_palindrome("A man a plan a canal Panaa"))