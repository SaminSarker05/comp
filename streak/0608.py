class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0

        # 0. hashmap to store each digit frequency
        freq = defaultdict(int)
        freq[0] = 1  # add 0 as a remainder by default
        running = 0

        # 1. loop through nums
        for num in nums:
            # 2. add current num to running sum
            running += num
            # 3. check if remainder was seen already
            res += freq[running % k]  # 4. if seen add how many times that remainder occured
            # 4. update the remainder freq
            freq[running % k] += 1
        return res
