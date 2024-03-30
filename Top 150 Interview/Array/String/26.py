class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        index = 1
        # 1. since sorted array unique if not equal to previous
        for i in range(1, len(nums)):
            # 2. if unique add to valid index and increment pos
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1
        return index
        


        # 1. use a set to store seen elements
        seen = set()
        index = 0
        for i in nums:
            # 2. if element was not seen set to a valid index
            if i not in seen:
                nums[index] = i
                index += 1
            seen.add(i)
        # return last index = unique numbers
        return index

        