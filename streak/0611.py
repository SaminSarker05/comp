class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # 0. make arr2 into a set for O1 lookup
        appear = set(arr2)
        res = []
        # 1. create a hashmap to store freq of each num
        freq = collections.defaultdict(int)

        other = []

        # 2. sepearte nums not in arr 2
        for num in arr1: 
            freq[num] += 1
            if num not in appear:
                other.append(num)

        # 3. add to res the freq of each elem in arr2 in same order
        for val in arr2:
            res.extend([val] * freq[val])
        
        # 4. add sorted remaining nums
        other.sort()
        res.extend(other)

        return res
