class Solution(object):
    def isValid(self, s):

        # use stack to keep track of left parenthesis and expected
        # use dict to keep track of different brackets
        stack = []
        brackets = {
            ']':'[',
            ')':'(',
            '}':'{'
        }

        for i in s:
            if i not in brackets:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if brackets[i] != last:
                    return False
        
        return len(stack) == 0