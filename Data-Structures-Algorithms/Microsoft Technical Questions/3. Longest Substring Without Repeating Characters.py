"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
"""

#Aproach
#1- Set a variable to store the maximun_len, another variable to store the current_len and a hasmap to keep track of the elementn we have visited
#2- loop through the array with two pointers, left is going to be pointing at the begginig of the substring and right is going to be pointed to the end of the sublist, and if the element not in hashmap just add it (maybe a set will be more suitable because we do not extra information, we just need to know if the element is in hashmap), if the element already in hashmap then we save the curret_len and we update ourhapmap to be empty

def longest_substring(s):
    max_length = 0
    left,right = 0, 0
    hashmap = {}
    while left < len(s) and right < len(s):
        if s[right] not in hashmap:
            hashmap[s[right]] = True
            right += 1
        else:
            max_length = max(max_length, right - left)
            hashmap = {}
            left += 1
    return max_length

s = "abcabecbb"
longest_substring(s)

s = "bbbbb"
longest_substring(s)


def longest_substring(s):
    max_length = 0
    left = 0
    hashmap = {}
    for right in range(len(s)):
        if s[right] in hashmap:
            left = max(left, hashmap[s[right]] + 1)  # Move left pointer to the right of the last occurrence
        hashmap[s[right]] = right  # Update the last occurrence of the character
        max_length = max(max_length, right - left + 1)  # Update max_length if needed
    return max_length

#Key important details about my wrong approach.
#1-- everytime you heard the word substring you need to have in mind sliding window techinique
#2-- is not necesary to delete the entire hashmap every time you find a character that is already in the hashmap, you just need to move the left pointer to points to the one step to the right of the last ocurrecen that way you do not need to worry about deleting the elements in the hashmap you just need to know if the new element of the sliding window is in the hasmap if it is for sure was in some other part of the window so you just update the left pointer to get rid of that element
#3-- a key important detail is how the left pointer moves, you need to move every time you find an element in the hashmap to the right, it is not correct to move it at the right pointer left = right because you probably can skip possible windows that could be the max length of the substring

"""
A really key important detail is how the sliding window works.

1- In this case the right pointer have a really simple behaviour, it just continue adding one element to the substring, it just expand the window by one, unlike the left pointer which have a behaviour that depends on a condition, the left pointer move one step to the right of the repeting element, sometimes the repeting element is at the beggining so we just move one step to the right but sometimes the repeting element could be at ith position so we move ith + 1 to the right.

There are two ways to move the left pointer based on a condition.

1- The first approach is to use a hashmap to store the position of the characters, so when we find a repeating character we just update the left pointer to move one step to the rigth of that position

hashmap = {}
left = 0
max_len = 0
for right_pointer in range(len(s)):
    if s[right] in hashmap:
        left = max(left, hashmap[s[right]] + 1) #We set the value of left using the info of the hashmap s = "abba"
    
    hashmap[s[right]] = right #Update the position of the character or just append a character that is not in the hashmap

    max_len = max(max_len, right - left + 1)

return max_len

2- the second and the most intuitive way is to use a while loop to move the left pointer one step at a time until it meets the condition, in this case is not necessary to use a hashmap because we are not going to need extra information about the position of the elements

chars = set()
left = 0
max_len = 0
for right_pointer in range(len(s)):
    while s[right] in set: #we continue updating left one step to the right until it meet the condtion
        char.remove(s[left]) #we remove value from the set until the s[right] element is a unique value, we start removing from the left until we find the repeating character and remove it from the set, when that happens the condition s[right] in set is going to be false
        left += 1
    
    char.add(s[right])
    max_len = max(max_len, right - left + 1)
return max_len
"""