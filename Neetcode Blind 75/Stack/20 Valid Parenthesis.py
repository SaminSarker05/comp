'''
time complexity: O(n) 
space complexity: O(n) - max space for stack
'''

class Solution(object):
    def isValid(self, s):

        # use hashmap to map closing and opening parenthesis
        brackets = {
            ']':'[',
            ')':'(',
            '}':'{'
        }

        # use stack to track expected opening parenthesis
        stack = []
        for char in s:
            if char in brackets:
                if len(stack) == 0 or stack.pop() != brackets[char]:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0