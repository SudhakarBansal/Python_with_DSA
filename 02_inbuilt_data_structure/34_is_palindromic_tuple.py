# Palindromic Tuple

# Input: ('a', 'b', 'c', 'b', 'a')
# Output: True

def is_palindromic_tuple(tup):
    start = 0
    end = len(tup) - 1

    while start <= end:
        if tup[start] != tup[end]:
            return False
        start += 1
        end -= 1

    return True

print(is_palindromic_tuple(('x', 'y', 'z', 'x')))