class Solution:
    def minNumberOperations(self, target: List[int]) -> int:

        # faster way to track ? subarrays ?
        # DP ?
        # 2d ? 

        # scan array to find subarrays that need updates
        next_val = 1
        moves = 0
        n = len(target)
        curr = [0] * n

        # TLE
        while True:
            moves += 1
            flag = False
            for i in range(n):
                if target[i] - curr[i] >= 1:
                    curr[i] += 1
                    flag = True
                elif flag:
                    break
            if curr == target:
                break

        return moves


        
