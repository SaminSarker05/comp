class Solution(object):
    def isIsomorphic(self, s, t):
        if len(set(s)) != len(set(t)) or len(s) != len(t): return False
        mapping = {}
        for i in range(len(s)):
            char = s[i]
            if char not in mapping:
                mapping[char] = t[i]
                continue
            
            if char in mapping and mapping[char] != t[i]: return False

        return True

"""
- check if same # of unique characters and length of strings
- check that each char maps to expeced in ordering
"""
