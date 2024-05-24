class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target: return [l+1, r+1]
            if total > target: r -= 1
            else: l += 1

"""

- use two pointers starting at left and right to compute running sum
- move left/right pointers depending on comparison of running sum and target
"""