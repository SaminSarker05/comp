class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        # 1. use set to keep track of seen values
        store = set()
        for i in nums:
            # 2. if values appear again add to answer
            if i in store:
                res.append(i)
            store.add(i)
        return res


        res = []
        for i in nums:
            # 1. use every element value as index 
            index = abs(i) - 1
            # 2. check if mapped index negative
            if nums[index] < 0:
                res.append(abs(i))
            else:
                # 3. negate new found values
                nums[index] *= -1
        return res
        