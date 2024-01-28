'''
time complexity: O(n) 
space complexity: O(n) - set seen incremented
'''

class Solution(object):
    def containsDuplicate(self, nums):

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False