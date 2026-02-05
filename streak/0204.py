class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        for i in range(n):
            if nums[i] < 0:
                newInd = (i - abs(nums[i])) % n
                result[i] = nums[newInd]
            elif nums[i] > 0:
                newInd = (i + abs(nums[i])) % n
                result[i] = nums[newInd]

        return result
        
