class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        flag = False
        # 1. loop backward to count characters
        for i in range(len(s)-1, -1, -1):
            # 2. if space after characters return count
            if flag and s[i] == ' ':
                return count
            # 2. when first char found change flag and increment count
            if s[i].isalpha():
                count += 1
                flag = True
        return count
        