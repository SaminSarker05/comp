class Solution(object):
    def lengthOfLIS(self, nums):
        # 0. DFS approach
        # 1. go backward to see if increase
        
        dp = [1] * len(nums)
        # 2. start value 1 since subarray of itself


        for i in range(len(nums)-1, -1, -1):
            # 3. generate subarrays going backward
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    # 4. if valid then increment count at index i
                    dp[i] = max(dp[i], 1 + dp[j])
        
        # 5. return max in tabulation
        return max(dp)

        