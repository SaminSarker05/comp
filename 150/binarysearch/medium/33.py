class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        # 0. binary search algo since time complexity
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            # 0. left side is sorted
            if nums[left] <= nums[mid]:
                # 1. check if target within sorted range
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else: left = mid + 1
            # 2. right side is sorted
            else:
                # 3. check if target within sorted range
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else: right = mid - 1
        return -1