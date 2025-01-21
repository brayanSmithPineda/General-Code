# Given a roman numeral, convert it to an integer.
# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

def romanToNumber(s):
    hash_map =  {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}
    result = 0
    for i in range(len(s)):
        if i+1 < len(s) and hash_map[s[i]] < hash_map[s[i+1]]:
            result -= hash_map[s[i]]
        else:
            result += hash_map[s[i]]
    return result
