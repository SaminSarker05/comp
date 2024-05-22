'''
time complexity: O(n) 
space complexity: O(1) - no change in sizes
'''

class Solution(object):
    def isAnagram(self, s, t):
        hashS, hashT = defaultdict(int), defaultdict(int)
        for char in s:
            hashS[char] += 1
        for char in t:
            hashT[char] += 1
        return hashS == hashT
        
"""
- create hashmaps of each string and return if identical
"""