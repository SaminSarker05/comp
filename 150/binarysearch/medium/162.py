class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 0. time complexity suggests binary search

        # 1. base case
        if len(nums) == 1: return 0

        left = 0
        right = len(nums) - 1
        # 2. binary search algo to find peak
        while left < right:
            mid = (left + right) // 2
            # 3. if mid greater than peak on left side
            if nums[mid] > nums[mid + 1]:
                right = mid
            # 4. if mid less than peak on right side
            else: left = mid + 1
        # 5. left points to the peak at end
        return left

        # O(n) WORKS BUT DOESNT MEET TIME 
        for i, num in enumerate(nums):
            if i != 0 and not (num > nums[i - 1]): 
                return i - 1
        

        # O(n) WORKS BUT DOESNT MEET TIME 
        for i, num in enumerate(nums):
            flag = True
            if i - 1 >= 0 and nums[i - 1] >= num: flag = False
            if i + 1 < len(nums) and nums[i + 1] >= num: flag = False
            
            if flag: return i