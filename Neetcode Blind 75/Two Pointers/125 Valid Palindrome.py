'''
time complexity: O(n) 
space complexity: O(1) - constant space use
'''

class Solution(object):
    def isPalindrome(self, s):

        l, r = 0, len(s) - 1
        # check if alpha numberic inside loop and if not adjust left and right
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
            