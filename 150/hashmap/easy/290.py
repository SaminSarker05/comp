class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(' ')
        if len(pattern) != len(words): return False

        i = 0
        mapping = {}
        seen = set()
        
        for char in pattern:
            if char not in mapping:
                if i >= len(words) or words[i] in seen: return False
                mapping[char] = words[i]
                seen.add(words[i])
            if mapping[char] != words[i]:
                return False
            i += 1
        return True

"""
- check if len of pattern and string match
- check that key val pair corresponds in string and same length
"""