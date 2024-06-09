class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        # 0. binary search algo to find min
        while left < right:
            mid = (left + right) // 2
            # 1. if mid > right than smallest on right
            if nums[mid] > nums[right]:
                left = mid + 1
            # 2. otherise min must be on left side
            else: right = mid

        return nums[left]