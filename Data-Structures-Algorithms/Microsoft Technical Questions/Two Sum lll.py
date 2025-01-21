"""
Problem Statement:
Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]

Output
[null, null, null, null, true, false]

Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false
"""
class TwoSum:
    def __init__(self):
        self.arr = []
    
    def add(self, element):
        self.arr.append(element)
    
    def find(self, target):
        hashmap = {}
        for index, element in enumerate(self.arr):
            x = target - element
            if x not in hashmap:
                hashmap[element] = index
            else:
                return True
        return False
    
#Although this solution works is best to use a hashmap insted of a list because every time we use the find function we are using extra space by creatign a hashmap
    
class Twosum:
    def __init__(self):
        self.hashmap = {}

    def add_element(self, element):
        if element not in self.hashmap:
            self.hashmap[element] = 1
        else:
            self.hashmap[element] += 1

        return self.hashmap
    
    def find(self, target):
        for i in self.hashmap:
            x = target - i
            if x in self.hashmap:
                if x != i or self.hashmap[i] > 1: #This condition ensure that if the complement is equal to the element then the element should be at list 2 because we can use the same element to sum up to the target, that's the reason why we store the count as the value in the dict
                    return True
        False

