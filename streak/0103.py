class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # prefix sum

        running = 0
        prefix = []
        # calculate the prefix sum for each index in the array
        for num in nums:
            running += num
            prefix.append(running)
        n = sum(nums)

        # caclulate the sum of the right elements or n - i - 1 elements
        right = [n - prefix[i] for i in range(len(nums))]

        res = 0
        for i in range(len(prefix) - 1):
            # if conditions meet increment the res value
            if prefix[i] >= right[i]:
                res += 1
        
        return res
