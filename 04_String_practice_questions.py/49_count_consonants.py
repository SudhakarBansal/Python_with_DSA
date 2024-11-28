# Count consonants in a string

# Input: "Python Programming"
# Output: 13

def count_consonants(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):  # Check if it's an alphabet
            if char not in vowels:
                count += 1
    return count

print(count_consonants("Python Programming"))


# pythonic way
# def count_consonants(s: str) -> int:
#     vowels = "aeiouAEIOU"
#     return sum(1 for char in s if char.isalpha() and char not in vowels)

