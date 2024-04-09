class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        # 1. use max heap since return order does not matter
        for x, y in points:
            # 2. dont need to square since all inputs squared
            dist = -(x*x + y*y)
            heapq.heappush(heap, (dist, [x,y]))
            # 3. if len greater than k for max heap pop biggest elem
            if len(heap) > k:
                heapq.heappop(heap)
        
        # 4. return coordinates for remaining in heap
        return [val[1] for val in heap]

        