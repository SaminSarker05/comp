class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t): return False
        if len(s) == len(t): return s == t

        p = 0
        for q in range(0, len(t)):
            if p > len(s) - 1: return True
            if t[q] == s[p]: p += 1
        
        return p == len(s)

"""
- use two pointers to track letters in s and t
- check lengths and valid index before indexing
"""