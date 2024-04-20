from collections import deque

class Solution(object):
    def coinChange(self, coins, amount):

        # BFS algo
        q = deque()
        # 1. bottom up iterative approach
        q.append((amount, 0))
        seen = set()
        # 2. use hashset for memoization
        while q:
            for _ in range(len(q)):
                # 3. if current val is negative of already seen pass
                val, depth = q.popleft()
                if val < 0 or val in seen: continue
                if val == 0: return depth
                seen.add(val)
                # 4. if new then add to set and add to queue
                for i in coins:
                    q.append((val - i, depth + 1))
        
        return -1