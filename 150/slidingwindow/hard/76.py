class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s): return ""

        mapping = defaultdict(int)
        for char in t: mapping[char] += 1
        required = len(set(t))

        running = defaultdict(int)
        l = 0
        res = len(s)
        ans = ""
        for r in range(len(s)):
            running[s[r]] += 1
            
            if s[r] in mapping and running[s[r]] == mapping[s[r]]:
                required -= 1
    
            while required == 0:
                if (r - l + 1) <= res:
                    res = r - l + 1
                    ans = s[l:r+1]
                
                running[s[l]] -= 1
                if s[l] in mapping and running[s[l]] < mapping[s[l]]:
                    required += 1
                l += 1
        return ans

"""
- use two dictionaries to track frequencies of chars
- see if better possiblity if all requirements meet
"""