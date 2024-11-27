#Count Vowels in a string

def count_vowels(s:str)->int:
    """
    Function to count the number of vowels in the input string.
    
    Parameters:
    s (str): The input string to check for vowels.
    
    Returns:
    int: The count of vowels in the input string.
    """
    # Your code here
    count = 0
    for char in s:
        if char in "aeiouAEIOU":
            count+=1
    return count

print(count_vowels("Hello, World!"))



# pythonic way:

# def count_vowels(s: str) -> int:
#     vowels = set("aeiouAEIOU")  # Using a set for faster lookup
#     return sum(1 for char in s if char in vowels)

# print(count_vowels("Hello, World!"))
