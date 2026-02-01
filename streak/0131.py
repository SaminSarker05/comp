class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # need to find smallest 2 numbers to the right of the first element
        # first element guarenteed to be start of first subarray
        a = float('inf')
        b = float('inf')
        for num in nums[1:]:
            if num < a:
                b = a
                a = num
            elif num < b:
                b = num
        
        return a + b + nums[0]


        # find group of smallest 3 #'s after one another

        # preprocessing to store smallest # to right for each number
        prefix = [-1] * len(nums)
        running = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] = running
            running = min(running, nums[i])

        # constraint small enough for nested loop aproach
        # fix one number and try all possible sums

        res = float('inf')
        # the first element will always be the start of one of the 3 subarrays

        for i in range(1, len(nums) - 1):
            t = nums[0] + nums[i] + prefix[i]
            res = min(res, t)
        
        return res

        
