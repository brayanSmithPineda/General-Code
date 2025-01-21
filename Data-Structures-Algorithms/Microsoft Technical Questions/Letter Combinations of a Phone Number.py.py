"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]
"""
def letterCombinations(digits):
    if not digits:
        return []
    
    # Mapping from digit to corresponding characters
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Resultant list to store the combinations
    result = []
    
    # Helper function to perform backtracking
    def backtrack(index, path):
        # If the path length is the same as digits length, append to result
        if len(path) == len(digits):
            result.append("".join(path))
            return
        
        # Get the letters that the current digit can represent
        possible_letters = phone_map[digits[index]]
        
        # Loop through these letters and recurse
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()  # Backtrack
    
    # Initialize backtracking
    backtrack(0, [])
    return result

# Example usage
print(letterCombinations("23"))
