class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0] * (n+1)
        for i in range(len(res)):
            num = i
            total = 0
            while num:
                total += num & 1
                num = num >> 1

            res[i] = total

        return res
        