class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # 1. use default dict to store frequency
        track = defaultdict(int)
        running_sum = 0

        # 2. calculate running sum and update freq for range(k) in nums
        for val in nums[:k]:
            track[val] += 1
            running_sum += val
        
        # 3. if k unique values then update res
        res = 0 if len(track) != k else running_sum

        # 4. fixed sliding window technique
        for r in range(k, len(nums)):
            # 5. add r and subtract l to simulate shift
            running_sum += nums[r]
            running_sum -= nums[r-k]

            # 6. update dictionary 
            track[nums[r]] += 1
            track[nums[r-k]] -= 1
            if track[nums[r-k]] == 0:
                del track[nums[r-k]]
            
            # 7. if k unique elemnts in dict then update res
            if len(track) == k:
                res = max(res, running_sum)
        
        return res


        