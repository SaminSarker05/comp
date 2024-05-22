'''
time complexity: O(n) 
space complexity: O(n)
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):

        seen = {}
        total = 0
        start = 0
        for i, val in enumerate(s):
            if val in seen and start <= seen[val]:
                start = seen[val] + 1
            else:
                total = max(total, i - start + 1)
            seen[val] = i
        return total