class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_cnt, max_n = 0, max(nums)
        res = 0
        l = 0
        # 1. sliding window 
        for r in range(len(nums)):
            if nums[r] == max_n:
                max_cnt += 1
            # 2. shrink window if extra nums or left num not max_n
            while max_cnt > k or (l <= r and nums[l] != max_n):
                if nums[l] == max_n:
                    max_cnt -= 1
                l += 1
            # 3. increment solution by left pointer and 1
            #    to hold all subarrays
            if max_cnt == k:
                res += l + 1
        
        return res



        # 1. brute force n^2 solution
        res = 0
        target = max(nums)
        # 2. generate all possible subarrays
        for i in range(len(nums)):
            count = 0
            for j in range(i, len(nums)):
                if nums[j] == target:
                    count += 1
                if count >= k:
                    res += 1
        return res





        # target = max(nums)
        # l, res = 0, 0
        # count = 0
        # # 1. sliding window to calculate subarrays
        # for i in range(len(nums)):
        #     # 2. if elem = max then increment count
        #     if nums[i] == target:
        #         count += 1
        #     # 3. while valid count increment left pointer
        #     while count >= k:
        #         # 4. update res e
        #         res += len(nums) - i
        #         if nums[l] == target:
        #             count -= 1
        #         l += 1
        # return res


        