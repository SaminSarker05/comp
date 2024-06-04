from collections import deque

class Solution(object):
    def coinChange(self, coins, amount):

        # 0. base cases
        if amount == 0: return 0
        if amount in coins: return 1

        # 1. bfs algo for dp problem
        q = deque()
        q.append([0, 0])
        
        # 2. set for memoization and memory optimzation
        seen = set()

        while q:
            # 3. pop last element and get running sum and depth or coin count
            val, depth = q.popleft()
            # 4. if amount was already seen or exceeds amount skip
            if val > amount or val in seen: continue

            # 5. if amount = target return number of coins
            if val == amount: return depth
            seen.add(val)
            for c in coins:
                q.append((val + c, depth + 1))
        
        return -1