"""
151. Reverse Words in a String

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
"""
s = "brayan smith"


#The idea i have is to add each word to a list and then reverse the string and then conver the string, but i do not know two things:
# 1- How to convert and put the words into a list, i know how to put each letter into a list, but i do know how to put each each word into the list maybe using the space but i do not know how, i also think that list() method to convert a string into a list is an O(n) time complexity and i think there is an efficient method
# 2 - I think we should use the spaces with two pointers but i do not came up with a clear idea 

#3 - You also have to remove leading or trailing spaces, how do i do that without removing the spaces that are in the middle?


s = 'brayan'
s[0] = 1
s

#have two pointers, the left pointer is going to pointer at the the start of a new word, this pointer is going to be in charge of eliminating the leading spaces and also determine when a new word start, this pointer will start at the beginning of the string. The right pointer will be at letf+1 and is going to determine the end of a word, we know the end of a word when right is equal to a space so that's when we reach the end, so if we do slicing string[i:j] we can have a word
#Then we are going to have a variable that is going to store our result variable, this is going to be a string that is going to be storing all the words that we encounter with our left and right pointers

#The key in this probelm is to use the two pointer two point to the start and end of the word, the spaces were used as continios of the while loops we use to update the two pointers
def reverseWords(s):
    left = 0    
    result = []

    while left < len(s):
        #Find the start of a word
        while left < len(s) and s[left] == ' ':
            left += 1
        #If we reach the end of the string we get out of the loop
        if left >= len(s):
            break
        #Find the end of a word
        right = left + 1
        while right < len(s) and s[right] != ' ':
            right += 1
        
        #Append the word to the list, right now the words have the same order it have in the string
        result.append(s[left:right])
        left = right + 1 

    return ' '.join(reversedList(result))


def reversedList(list):
    left, right = 0, len(list)-1
    while left <= right:
        list[left], list[right] = list[right], list[left]
        left += 1
        right -= 1


s = 'brayan smith pineda duarte'

reverseWords(s)


#If a while loop ends because one of the condition is not met, let's say j != 1 was one of the condition of the while loop and right now j = 1 so while loop stops later in the function i update the value of j to 0, the while loop start executing again because now j meet the condition or it does not execute because j was updated after the while loop


#In this problem i learn two things:
##1- when i while loop ends because one of the condition is not met it will not restart if later in the function the condtion is change and met the while loop, so if while j!=0: and right now j =0 the while stop, and later you change j = 1 the while will now start executing again unless you put all you body cody in an outter while loop
##2- if one of you variable depends on the value of anoter variable, this first variable will not be updated automatically is the value of the conde value change, it has to be inside a loop so every time the loop is executed variable1 = variable2 + 1 will run an update the value.
##3- ALWAYS write the the condtion that checks that the index is not outbound first, if you do s[i] and i < len(s) first is going to execute the first condition and if i is out of bound we will get an index error.
##4 - As strings are immutable, concatenation is a quadratic time complexity operation because each time you concatenate two strings you have to create a new one to hold the result and then copying each charecter from the original string, a better way to cancetenate string will be to pass each string to a list and the ''.join() which take linear time O(n).
# result = ""
# for char in ["a", "b", "c", "d", ...]:  # Imagine this continues for n characters
#     result += char
# First Iteration: Copy 'a' to result.
# Second Iteration: Copy 'a' and 'b' to a new string (2 operations: copy 'a' + copy 'b') and assign it to result.
# Third Iteration: Copy 'a', 'b', and 'c' to a new string (3 operations: copy 'a' + copy 'b' + copy 'c') and assign it to result.
# Fourth Iteration: Copy 'a', 'b', 'c', and 'd' to a new string (4 operations).
# By the time you reach the end of the string, the last concatenation operation alone involves copying all n characters to a new string. If you sum up the work done across all iterations, you get 1 + 2 + 3 + ... + n, which is the sum of the first n integers. This sum is (n * (n + 1)) / 2, which is O(n²).