# heap data structure
# min heap (default) or max heap
# root is min and max of each subtree


class MedianFinder(object):

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap
        # 0. len(small) should always be <= len(large)
        

    def addNum(self, num):
        # 1. python only has min heap so negate to simulate max heap
        heapq.heappush(self.small, -num)

        # 2. ensure every val in small <= large
        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            # 3. if invalid add largest number in small heap to large heap
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # 3. ensure size maintained
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (self.large[0] + (-1 * self.small[0])) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()