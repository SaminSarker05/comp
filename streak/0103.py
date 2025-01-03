class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # prefix with more work? yes
        running = 0
        prefix = []
        for num in nums:
            running += num
            prefix.append(running)
        n = sum(nums)

        right = [n - prefix[i] for i in range(len(nums))]

        res = 0
        for i in range(len(prefix) - 1):
            if prefix[i] >= right[i]:
                res += 1
        
        return res


        
