class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        start = ord(s[0])

        # 0. for loop from second char
        for i in range(1, len(s)):
            # 1. add difference of ascii value to res
            res += abs(ord(s[i]) - start)
            # 2. update first value
            start = ord(s[i])

        return res
