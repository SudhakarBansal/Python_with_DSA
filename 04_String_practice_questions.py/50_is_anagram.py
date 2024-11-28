#Check for anagrams

#Input: s = "anagram", t = "nagaram"
# Output: True

def is_anagram(s, t):
    """
    function to check if t is an anagram of s without using zip.
    
    Parameters:
    s (str): The first input string.
    t (str): The second input string.
    
    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """
    if len(s) != len(t):
        return False

    # Initialize a single frequency array
    char_count = [0] * 26  # For lowercase English letters

    # Process characters in s and t separately
    for i in range(len(s)):
        char_count[ord(s[i]) - ord('a')] += 1
        char_count[ord(t[i]) - ord('a')] -= 1

    # Check if all counts are zero
    for count in char_count:
        if count != 0:
            return False

    return True
     
print(is_anagram("anagram","nagaram"))