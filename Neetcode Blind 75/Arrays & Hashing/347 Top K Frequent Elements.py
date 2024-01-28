'''
time complexity: O(n) 
space complexity: O(n) - at worst pushing to freq dict n times
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == len(nums):
            return nums

        freq = {}
        store = [[] for i in range(len(nums) + 1)] # list comprehension for distinct memory objects
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        # store freq via array index
        for key, val in freq.items():
            store[val].append(key)

        res = []
        for i in store[::-1]:
            for n in i:
                res.append(n)
                if len(res) == k:
                    return res
