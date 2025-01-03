class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        flag = False

        # 0. make dict to hold character frequencies
        freq = defaultdict(int)
        for char in s: freq[char] += 1
        

        for k, v in freq.items():
            # 1. if even # then can make palindrome of that len
            if v % 2 == 0: res += v
            # 2. if odd then add remaining even length to res
            else:
                res += v - 1
                # 3. mark possible center value if exists which does not need a pair
                flag = True
        
        return res + flag
