class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        star = []
        # 1. use stacks to store elements
        for i, val in enumerate(s):
            if val == '(':
                stack.append(i)
            elif val == '*':
                star.append(i)
            # 2. cancel right paren if available left paren or star
            elif val == ')' and stack:
                stack.pop()
            elif val == ')' and star:
                star.pop()
            # 3. if no available then return false
            elif val == ')':
                return False
        
        # 4. cancel extra left paren with star
        while stack and star:
            # 5. make sure index of star is greater than left paren
            if star[-1] < stack[-1]:
                return False
            star.pop()
            stack.pop()

        # 5. left and right paren must be canceled. star count does not matter
        return len(stack) == 0        
