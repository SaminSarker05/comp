class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                a1, a2 = s[l:r], s[l+1: r+1]
                return a1 == a1[::-1] or a2 == a2[::-1]
            
            l += 1
            r -= 1

        return True
            
        