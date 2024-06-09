class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # 0. combine elements into one array
        n3 = nums1 + nums2
        
        # 1. sort array nlogn
        n3.sort()

        # 2. if even then return avg of middle values
        if len(n3) % 2 == 0:
            mid = len(n3) // 2
            sums = n3[mid] + n3[mid - 1]
            sums = float(sums) / 2
            return sums

        # 3. if odd return middle value
        return n3[len(n3) // 2]