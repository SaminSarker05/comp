class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # 1. use given sizes to set indices
        i = m - 1
        j = n - 1
        k = m + n - 1
        # 2. process all elements of nums2
        while j >= 0:
            # 3. if i valid index and num1 elem larger do assignment
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            # 3. other cases decrement j and use nums2 element
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        return nums1


        k = len(nums1) - 1
        i, j = len(nums1) - n - 1, len(nums2) - 1
        # 1. start merging from greatest of each array
        while j >= 0 and i >= 0:
            if nums1[i] > nums2[j]:
                # 2. insert right element in each position
                nums1[k] = nums1[i]
                i -= 1
            else:
                # 3. if values equal or nums2 larger decrements nums2
                nums1[k] = nums2[j]
                j -= 1
            # 4. decrement k position each time
            k -= 1
        # 5. check to see all values in nums2 are processed
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

