class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        - only sorting 1 to N inclusive
        - ignore values outside range
        - for loop at end to find missing values
        '''

        i = 0
        # 1. cyclic sort to sort array 
        while i < len(nums):
            val = nums[i] - 1
            if nums[i] <= 0 or nums[i] > len(nums):
                i += 1
                continue
            # 2. if indexes do not match and unique swap then swap
            elif val != i and val < len(nums) and nums[val] != nums[i]:
                nums[i], nums[val] = nums[val], nums[i]
            else:
                i += 1
        # 3. if index not equal to element then return
        for i in range(1, len(nums) + 1):
            if nums[i-1] != i:
                return i
        
        return len(nums) + 1