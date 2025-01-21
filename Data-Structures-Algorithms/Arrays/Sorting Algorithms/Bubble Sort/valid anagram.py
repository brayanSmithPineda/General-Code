"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
"""

#Create a has_map to store the elements of s
#Then see if the the elements of t are in s

def angranm(s,t):
    hash_map = {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] not in hash_map:
            hash_map[s[i]] = 1
        else:
            hash_map[s[i]] += 1
    for j in range(len(t)):
        if t[j] not in hash_map:
            return False
        hash_map[t[j]] -=1
        if hash_map[t[j]] == 0:
            del hash_map[t[j]]
        
    return True
            
s = "ab"
t = "a"
angranm(s,t)

def isAnagram(s, t):
    # If lengths differ, they can't be anagrams
    if len(s) != len(t):
        return False
    
    # Initialize a count dictionary
    count = {}
    
    # Count characters in s
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    # Decrease count for characters in t
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] == 0:
            del count[char]
    
    # If count is empty, they are anagrams
    return len(count) == 0

# Test cases
print(isAnagram("anagram", "nagaram"))  # Output: True
print(isAnagram("rat", "car"))  # Output: False
