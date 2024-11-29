def is_substring(s: str, t: str) -> bool:
    """
    Function to check if string t is a substring of string s without using built-in functions and recursion.
    
    Parameters:
    s (str): The main string.
    t (str): The string to check as a substring.
    
    Returns:
    bool: True if t is a substring of s, False otherwise.
    """
    if len(t) == 0:  # An empty substring is always a substring
        return True
    if len(s) < len(t):  # If `t` is longer than `s`, it can't be a substring
        return False

    i = j = 0
    while i < len(s):
        print("i :",i,"j :",j)
        if s[i] == t[j]:
            j += 1  # Advance in `t`
            if j == len(t):  # Full match of `t` found
                return True
        else:
            # Reset `j` but handle partial matches
            i -= j  # Backtrack `i` to the start of the current potential match
            j = 0  # Reset `j`
        i += 1

    return False

print(is_substring("woworld","world"))
