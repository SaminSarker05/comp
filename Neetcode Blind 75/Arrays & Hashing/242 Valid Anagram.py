'''
time complexity: O(n) 
space complexity: O(1) - no change in sizes
'''

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        # sorted is nlogn time
        # faster to count unique values using set: O(n)
        
        for val in set(s):
            if s.count(val) != t.count(val):
                return False
        return True
