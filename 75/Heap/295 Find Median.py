import heapq

class MedianFinder:

    def __init__(self):
        self.minheap = [] # holds larger #s
        self.maxheap = [] # always has one more than minheap; holds smaller numbers
        

    def addNum(self, num: int) -> None:
        if not self.minheap or num <= -self.minheap[0]:
            heapq.heappush(self.minheap, -num)
        else:
            heapq.heappush(self.maxheap, num)

        if len(self.minheap) > len(self.maxheap) + 1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

        elif len(self.minheap) < len(self.maxheap):
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))



    def findMedian(self) -> float:

        if len(self.minheap) != len(self.maxheap):
            return -self.minheap[0]

        return (self.maxheap[0] + -self.minheap[0]) / 2.0