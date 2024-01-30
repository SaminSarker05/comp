'''
time complexity: O(n) 
space complexity: O(1)
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l, r = 0, len(height) - 1
        width = r - l
        res = 0
        while l < r:
            length = min(height[r], height[l])
            area = length * width
            res = max(area, res)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            width -= 1
        
        return res

        