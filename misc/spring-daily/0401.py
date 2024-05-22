class Solution(object):
    def isIsomorphic(self, s, t):
        # 1. check if len strings or # unique char match
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False
        
        # 2. use dict to hold mapping between chars
        hold = {}
        for i in range(len(s)):
            char = s[i]
            # 3. if new char add to dict
            if char not in hold:
                hold[char] = t[i]
                continue
            # 4. if seen and not matching return False
            if hold[char] != t[i]:
                return False
        
        return True
