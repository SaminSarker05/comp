class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # 0. edge cases if len nums is 0 or 1
        if len(nums) == 0: return []
        if len(nums) == 1: return [str(nums[0])]

        # 1. have a running interval and left and right pointers
        res = []
        left = 0
        running = nums[left]
        for right in range(1, len(nums)):
            # 2. if not expected value add current interval to res
            if nums[right] != running + 1:
                if nums[left] != running: 
                    val = str(nums[left]) + "->" + str(running)
                    res.append(val)
                else: res.append(str(running))
                left = right
                running = nums[left]
            # 3. if valid update running interval
            else: running = nums[right]
        
        # 3. check for last interval
        if nums[left] != running: 
            val = str(nums[left]) + "->" + str(running)
            res.append(val)
        else: res.append(str(running))
 
        return res