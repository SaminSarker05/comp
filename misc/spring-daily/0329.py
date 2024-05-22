class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # solves possible subarrasys with at most k
        def solve(k):
            res, l, = 0, 0
            store = {}
            # 1. sliding window technique
            for r in range(len(nums)):
                if nums[r] not in store:
                    store[nums[r]] = 0
                store[nums[r]] += 1
                # 2. shrink when more than k unique elements
                while len(store) > k:
                    store[nums[l]] -= 1
                    if store[nums[l]] == 0:
                        del store[nums[l]]
                    l += 1
                # 3. update res as r-l+1 possible valid subarrays
                res += r-l+1
            return res
        
        # 4. at most k - at most k-1 = k elements
        return solve(k) - solve(k-1)
            

            




        # 1. brute force
        res = 0
        for i in range(len(nums)):
            store = set()
            for j in range(i, len(nums)):
                store.add(nums[j])
                if len(store) == k:
                    res += 1
        return res

        