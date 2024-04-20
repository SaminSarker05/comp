class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """

        """
        thought process:
        - use dijkstra algo
        - let each coordinate have a distance (initially infinity)
        """

        m = len(heights)
        n = len(heights[0])

        q = []
        # 1. queue and heap for dijkstra algo
        q.append((0,0,0))
        # 2. hashset to track which coordinates seen
        seen = set() 

        while q:
            weight, x, y = heapq.heappop(q)
            if (x, y) in seen: continue

            # 3. if at bottom corner return its weight which has already been fixed
            if (x, y) == (m-1, n-1):
                return weight
            
            seen.add((x, y))
            # 4. loop through adjacent cells
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:
                    # 4. if valid coor, update effort as defined in problem
                    new_val = max(weight, abs(heights[nx][ny] - heights[x][y]))
                    # 5. add coor and effort to heap to continue
                    heapq.heappush(q, (new_val , nx, ny))

        return -1