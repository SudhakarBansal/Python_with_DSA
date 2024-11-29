# Roman to Integer

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

def romanToInt(s: str) -> int: 
    res = 0
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for i in range(0,len(s)):
        if i==len(s)-1:
            return res+ roman[s[i]]
        if roman[s[i]] >= roman[s[i+1]]:
            res += roman[s[i]]
        else:
            res -= roman[s[i]]
    return res

print(romanToInt("XL"))

