"""
5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.


Input: s = "cbbd"
Output: "bb"
"""
#There are two ways to check is a string is a palindrom, inward and outward approach, the #----Inward Approach: We use the pointers, one at the start and one at the end, then we starting to check every single letter inward by incrementing left and decrementing right.
#----Outward Approach: we use each letter of the string as a center, and then we set the left and right pointers to expand outwards from that center, if s[left] = s[right] then we just continue decrementing left and incrementing right until they're different. This approach is more efficient as it just traverse the string once and use each letter as a center and then expand to check for palindroms

#Inward approach
def longest_palindrom_inner_aproach(string):
    def isPalindrom(left, right):
        while left <= right:
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
    
    left = 0
    res = ""
    for left in range(len(string)):
        for right in range(left,len(string)):
            if isPalindrom(left, right):
                if (right - left + 1) > len(res):
                    res = string [left:right+1]
        left += 1





def longest_palindrom_outward_approach(string):
    def isPalindrom(left, right):
        while left >= 0 and right < len(string) and string[left] == string[character]:
            left -= 1
            right += 1
        return left + 1, right - 1
    res = ""
    for character in range(len(string)):
        left, right = isPalindrom(character, character) #this way you store the output of the function, left and right are initilize at the center of the character
        
        if (right - left+1) > len(res):
            res = string[left:right+1]

         # Check for even-length center palindromes
        if character + 1 < len(string):
            left, right = isPalindrom(character, character + 1)
            if (right - left + 1) > len(longest):
                longest = string[left:right+1]
    return res