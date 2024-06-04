class Solution(object):
    def permute(self, nums):

        # PERMUTATIONS
        # order does not matter

        res = []
        k = len(nums) # 0. store target length to know when to stop

        # 1. dfs algo to make all permuations
        def dfs(running):
            # 2. if length is met then add to res
            if len(running) == k:
                res.append(running[:])
                return
            # 3. loop through values and only add if not seen
            for val in nums:
                if val not in running:
                    running.append(val)
                    # 4. pass running array to recursive vall
                    dfs(running)
                    running.pop()
        dfs([])
        return res
      