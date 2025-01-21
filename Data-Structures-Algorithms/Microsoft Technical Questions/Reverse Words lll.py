"""
557. Reverse Words in a String III
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"
"""



#Append all the letter to a list
#Loop through the list with two pointers, the left pointer is going to point at the beggining of a word and the right pointer is going to be pointing at the end of a word, once we have a word we just reversed() and .join() to convert it back to string

def reversedwords(s):
    letters = []
    result = []
    for i in s:
        letters.append(i)
    left = 0
    while left < len(letters):
        while left < len(letters) and letters[left] == ' ':
            left+=1

        if left >= len(letters):
            break

        right = left + 1
        while right < len(letters) and letters[right] != ' ':
            right += 1
        
        word = letters[left:right]
        word.reverse() # Reverse the list in place
        result.append(''.join(word)) #Right now word is a list of letters of the word, as we want to append the the result the entire word and not the letter itself we have to join the letters(each element of the word list) and then append it to the result 

        left = right + 1
    return ' '.join(result)

s = "Let's take LeetCode contest"
reversedwords(s)


reversed(s)
s


#Things i learned:
#--1 the reverse() method reverse the list in place so when you do words = s.reverse() you reverse s in place and words is None right now beacause that's what reverse return, so when you try to append this word to the result list is going to append None and not the reverse word.

s = [1,2,3,4]
w = reversed(s)
w

def reversedWords2(s):
    letters = list(s)  # You can directly convert string to list
    result = []
    left = 0
    while left < len(letters):
        # Skip leading spaces
        while left < len(letters) and letters[left] == ' ':
            result.append(letters[left])
            left += 1
        
        # If we've reached the end of the string, stop
        if left >= len(letters):
            break

        # Find the end of the current word
        right = left + 1
        while right < len(letters) and letters[right] != ' ':
            right += 1
        
        # Extract and reverse the word
        word = letters[left:right]
        result.append(''.join(reversed(word))) 

        # Move to the next word
        left = right
    
    return ''.join(result)

s = "Let's take LeetCode contest"
reversedWords2(s)

def reversedWords3(s):
    letters = []
    for i in s:
        letters.append(i)
    left = 0
    while left < len(letters):
        while left < len(letters) and letters[left] == ' ':
            left+=1
            
        if left >= len(letters):
            break

        right = left + 1
        while right < len(letters) and letters[right] != ' ':
            right += 1
        
        temp_left = left
        temp_right = right - 1
        while temp_left <= temp_right:
            letters[temp_left], letters[temp_right] = letters[temp_right], letters[temp_left]

            temp_left += 1
            temp_right -= 1

        left = right + 1
    return ''.join(letters)

s = "Let's take LeetCode contest"
reversedWords3(s)


def reverseWordsInString(s):
    words = []
    i = 0

    while i < len(s):
        if s[i] == ' ':
            words.append(' ')
            while i < len(s) and s[i] == ' ':
                i += 1
        else:
            start = i
            while i < len(s) and s[i] != ' ':
                i += 1
            words.append(s[start:i][::-1])  # Slice the word and reverse it

    return ''.join(words)
