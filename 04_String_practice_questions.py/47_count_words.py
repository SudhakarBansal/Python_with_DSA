# Count words in a string
def count_words(s):
    """
    Function to count the number of words in the input string without using built-in functions.
    
    Parameters:
    s (str): The input string to check for words.
    
    Returns:
    int: The count of words in the input string.
    """
    count = 0  # Initialize a counter for the number of words
    in_word = False  # Flag to track if we are inside a word
    
    # Loop through each character in the string
    for char in s:
        # Check if the character is not a space
        if char != ' ':
            if not in_word:  # If we were not in a word before
                in_word = True  # Set the flag to indicate we are now in a word
                count += 1  # Increment the word count
        else:
            in_word = False  # If we encounter a space, we are not in a word anymore
    
    return count  # Return the total count of words


print(count_words("Hello, World!"))


# pythonic way :

# def count_words(s:str)->int:
#     return len(s.split())
