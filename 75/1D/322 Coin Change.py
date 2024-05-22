from collections import deque

class Solution(object):
    def coinChange(self, coins, amount):

        hold = deque()
        hold.append(amount)
        depth = 0
        seen = set() # memoization

        # BFS ALGO
        while hold:
            for _ in range(len(hold)):
                first = hold.popleft()
                if first == 0:
                    return depth
                if first < 0:
                    continue
                if first not in seen:
                    seen.add(first)
                    for i in coins:
                        hold.append(first - i)
            
            depth += 1

        return -1
        


