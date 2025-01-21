"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
"""

def validAnagram(s, t):
    for character in s:
        sorted_s = sorted(s)
    for character in t:
        sorted_t = sorted(t)
    return sorted_s == sorted_t

#Time complexity O(NlogN)
s = "anagram"
t = "nagarrm"

validAnagram(s,t)

def validAnagram2(s,t):
    if len(s) != len(t):
        return False
    frecuency = [0] * 26
    for character in s:
        frecuency[ord(character) - ord('a')] += 1
        
    for character in t:
        frecuency[ord(character) - ord('a')] -= 1
        if frecuency[ord(character) - ord('a')] < 0  :
            return False
   
    for c in frecuency:
        if c != 0:
            return False
    return True

s = "anagram"
t = "nagarrm"

validAnagram2(s,t)