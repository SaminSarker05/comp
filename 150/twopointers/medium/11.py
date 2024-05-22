class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        total = 0
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            if w * h > total: total = w * h
            if height[l] < height[r]: l += 1
            else: r -= 1

        return total

"""
- calculate height and width in each iteration
- keep max height and increment l/r pointers
"""