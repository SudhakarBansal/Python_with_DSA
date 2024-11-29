# Check Subsequencerem

# Input: s = "abcde", t = "ace"
# Output: True
 
# Input: s = "abcde", t = "aec"
# Output: False
def is_subsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)    


print(is_subsequence("aaaaaa","bbaaaa"))