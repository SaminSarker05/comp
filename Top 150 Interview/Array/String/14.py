class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 1. if no strings return 0
        if len(strs) == 0: return 0

        # 2. find smallest string as that is max longest common prefix
        compare = min(len(s) for s in strs)
        res = ""
        # 3. loop through smallest string
        for i in range(compare):
            curr = strs[0][i]
            # 4. loop through each string to compare char
            for string in strs:
                # 5. if not equal then return current prefix
                if string[i] != curr:
                    return res
            # 6. otherwise add shared char to solution
            res += curr
        return res

 
        