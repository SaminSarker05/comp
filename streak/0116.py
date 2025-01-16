class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # important properties of xor (cummutative):
        #   xor with 0 results in same number
        #   xor with itself resuts in 0

        # use algebra to rearrange
        # (a1 ^ b1) ^ (a1 ^ b2) ^ (a2 ^ b1) ^ (a2 ^ b2)
        # (a1 ^ a1 ^ ... repeated n2 times) ^ (a2 ^ a2 ^ ... repeated n2 times) ^ 
        # (b1 ^ b1 ^ ... repeated n1 times) ^ (b2 ^ b2 ^ ... repeated n1 times)

        # each element in nums1 xor with self n2 times
        # each element in nums2 exor with self n1 times

        # find frequency of each number in nums1 and nums2
        # if even frequency then no contribution; otherwise contributes value to res

        res = 0

        dict1 = {}
        for i in range(len(nums1)):
            if nums1[i] not in dict1:
                dict1[nums1[i]] = 0
            dict1[nums1[i]] += len(nums2)
        
        dict2 = {}
        for i in range(len(nums2)):
            # practice using get method dict.get(key, default_value)
            dict2[nums2[i]] = dict2.get(nums2[i], 0) + len(nums1)
        
        for key, val in dict1.items():
            if val % 2 == 0: continue
            res ^= key
        
        for key, val in dict2.items():
            if val % 2 == 0: continue
            res ^= key
        
        return res


    

        # brute force ? TLE
        res = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                res ^= nums1[i] ^ nums2[j]
        
        return res

        
