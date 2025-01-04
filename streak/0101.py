class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        ones = 0
        res = 0

        # track the number of ones on the right hand side
        for char in s:
            if char == '1':
                ones += 1
        
        # since split must be non-empty skip last char
        for char in s[:-1]:
            if char == '0':
                zeros += 1
            elif char == '1':
                ones -= 1

            # update the left and right side count of zeros and ones and then maximizes res
            res = max(res, ones + zeros)
        
        return res
