from collections import deque

class Solution(object):
    def coinChange(self, coins, amount):
        
        if amount == 0:
            return 0
        if amount in coins:
            return 1

        # BFS algorithm; prune visited branches; keep track of depth

        track = deque()
        track.append(amount)
        depth = 0
        seen = set()

        while track:
            for j in range(len(track)):
                last = track.popleft()
                if last < 0:
                    continue
                elif last == 0:
                    return depth
                if last not in seen:
                    seen.add(last)

                    for i in coins:
                        track.append(last - i)
                
            depth += 1
        
        return -1