class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # O(n) solution two pointers
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1
        i = n - 1

        nums = [j*j for j in nums]
        # 1. list comprehension to square all elements

        while l <= r: # <= since can be identical
            # 2. add in increasing order to res array
            if nums[l] > nums[r]:
                res[i] = nums[l]
                l += 1
            else:
                res[i] = nums[r]
                r -= 1
            i -= 1

        return res



        # TRIVIAL approach nlogn
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        
        nums.sort() # sorting takes nlogn
        return nums
        