class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1: return len(s)

        seen = set()
        seen.add(s[0])
        res = 1
        l = 0
        for r in range(1, len(s)):
            if s[r] not in seen:
                res = max(res, r - l + 1)
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
        
        return res

"""
- need to find longest substring
- if repeating then keep removing till corrected
"""