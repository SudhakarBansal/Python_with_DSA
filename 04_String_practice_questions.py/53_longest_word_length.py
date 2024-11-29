# Length of the Longest Word

#Input: s = "The quick brown fox jumps over the lazy dog"
# Output:5


def longest_word_length(s):
    max_length = 0  # To store the length of the longest word
    current_length = 0  # To store the length of the current word

    for char in s:
        if char != ' ':  # If the character is not a space, it's part of a word
            current_length += 1
        else:
            # When a space is encountered, compare and reset current_length
            max_length = max(max_length, current_length)
            current_length = 0

    # Check the last word (if there is no trailing space)
    max_length = max(max_length, current_length)

    return max_length

# Example usage
print(longest_word_length("The quicssk brown fox jumps over the lazy dogsdvadv"))




# pythonic way :

# Input: s = "The quick brown fox jumps over the lazy dog"
# Output:5


# def longest_word_length(s:str)->int:    
#     s = set(s.split())
#     max_count=0
#     for char in s:
#         max_count=max(len(char),max_count)
#     return max_count
