"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

#The problem here is first how to identify with code that two strings are anagrams without traversing each words of the strings, the solution is that since anagrams have the same letters just in different order we can just sort the strings that way we can identify which words are anagrams.

#The second was how to group them once we indentify two words are anagram, the key here is that hashmap can have as keys the sorted string and as value a list of words, so we just have to see if the word when sorted is equal to the key and if it is the we just added to the list

#Here is the algorithm:
# -- Loop throgh every word of the list
# -- sort the word and if the sorted word not in hashmap then as key the sorted word and as value a list of the actual word
# -- if we sort the word and the is in hashmap then we just append the actual word to the list

def groupAnagram(srts):
    hashmap = {}
    
    for word in srts:
        sorted_word = sorted(word) #Sorted function returns always a list of the itarable, and we can not pass a list as a key for a hashmap, we got this TypeError: unhashable type: 'list', so we have to conver the sorted_word back to a string
        key = ''.join(sorted_word)

        if key in hashmap:
            hashmap[key] += [word]
        else: 
            hashmap[key] = [word]
    return list(hashmap.values())

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagram(strs)

#Things a learng

#sorted(s) returns a always a list of the iterable
#hasmap can not store a list as a key, but its value can be a key
#hashmap.values() return the dict_values of the hashmap, we have to convert it to list() to be able to return a list
#+= does not intilize any data structure, this assume that the data structure already exist and we are going to append the new value

#the time complexity of this solution is O((N⋅WlogW)) WlogW is for the sorting part and the N for the joining string part

#we can have a more efficient solution if we can skip the sorting part that we write as the key for the hashmap, what we can do instead is to count the frecuency of each character in the string and have it as key.This way, the key represents a unique identifier for the anagram group.

#Crete hashmap
#how to we count the freacuency of each character in a word: we use a double for loop, one for the word, and the inner for the character, we create a list of 26 0 elements, this represent the 26 letters of the alphabet, and they are initilize as ceros because we haven't the frecuency of the character yet.
#How to we start counting the frecuency, we just used count[] += 1, how to we now in which poistion put each character, we just ASCII values with ord() method

def groupAnagram2(s):
    hashmap = {}
    for word in s:
        count = [0]*26 # 26 letter of the alphabet
        for character in word: #count the frecuency of each character in the current word
            count[ord(character) - ord('a')] += 1
        
        #we convert out list into a tuple, so we don't get the key Error for not hashable data
        frecuency_key = tuple(count)

        if frecuency_key in hashmap:
            hashmap[frecuency_key].append(word)
        else:
            hashmap[frecuency_key] = [word]
    return list(hashmap.values())


strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagram2(strs)