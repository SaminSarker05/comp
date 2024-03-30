class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 1. use flag to assign in array and freq of nonval values
        valid = 0
        # 2. loop through to find elements not equal to vald
        for i in nums:
            if i != val:
                # set element to be at a valid position
                nums[valid] = i
                valid += 1
        return valid

        