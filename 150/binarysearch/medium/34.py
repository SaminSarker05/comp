class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 0. helper func using binary search to find elem
        def helper(nums, target, flag):
            left = 0
            right = len(nums) - 1
            # 1. if elem never found return -1
            ind = -1
            while left <= right:
                mid = (left + right) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                # 2. if elem found keep searching left or right side for elem
                else:
                    # 3. record last seen ind of elem
                    ind = mid
                    if flag: right = mid - 1
                    else: left = mid + 1
            return ind

        # 4. look for elem and use flag to denote first or last pos
        l = helper(nums, target, True)
        r = helper(nums, target, False)
        return [l, r]