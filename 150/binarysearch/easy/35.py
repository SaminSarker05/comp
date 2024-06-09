class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # 0. logn time requirement -> binary search HINT
        # 1. index question would be output of binary search algo; SORTED input as well

        left = 0
        right = len(nums) - 1

        # 2. binary search algo
        while left <= right:
            # 3. calculate mid and compare with target
            ind = (right + left) // 2
            if target == nums[ind]: return ind
            if target < nums[ind]:
                right = ind - 1
            else:
                left = ind + 1

        # 4. if never found then target would be at left which has pos now greater than right
        return left