class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1. use strip to remove leading and trailzing spaces
        s = s.strip()
        res = 0
        for c in s:
            # 2. if space then reset frequency
            if c == ' ':
                res = 0
            # 3. otherwise add to res
            else:
                res += 1
        return res
        