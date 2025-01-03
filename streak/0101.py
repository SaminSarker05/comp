class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        ones = 0
        res = 0

        for char in s:
            if char == '1':
                ones += 1
        
        for char in s[:-1]:
            if char == '0':
                zeros += 1
            elif char == '1':
                ones -= 1

            res = max(res, ones + zeros)
        
        return res

        
