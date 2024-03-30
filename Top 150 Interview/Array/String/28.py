class Solution(object):
    def strStr(self, haystack, needle):
        # 1. only need to check length difference between haystack and needle
        for i in range(len(haystack)-len(needle)+1):
            # 2. if valid start and end then loop check string splice equality
            if i + len(needle)-1 < len(haystack) and haystack[i] == needle[0] and haystack[i+len(needle)-1] == needle[-1]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        
        return -1