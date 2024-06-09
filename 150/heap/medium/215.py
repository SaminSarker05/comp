class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """ TIME COMPLEXITIES
        - geting min O(1)
        - insertion O(logn)
        - deletion O(logn)
        """

        # 0. use heap to store elements
        heap = []
        for num in nums:
            # 1. negative elements to make a max heap
            heapq.heappush(heap, -num)
        
        # 2. remove k - 1 elems from heap
        while k - 1:
            heapq.heappop(heap)
            k -= 1

        # 3. return kth elem; negate to make back to original num
        return -heapq.heappop(heap)