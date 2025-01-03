class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # 0. use two pointers to check characters in s and t
        p1, p2 = 0, 0
        while p1 < len(s) and p2 < len(t):
            # 1. if same character bump both pointers
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            # 2. if not equal keep looking for char in s
            else: p1 += 1
        # 3. length remaining in t is what must be appended
        return len(t[p2:])
