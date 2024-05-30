class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # 0. set to hold operands for constant look up
        operands = set(["/", "-", "+", "*"])
        stack = [] # 1. stack will hold digits
        for token in tokens:
            # 2. if token is digit then add to stack
            if token not in operands:
                stack.append(int(token))
                continue
            # 3. if operand then pop last two and perform operation
            v1 = stack.pop()
            v2 = stack.pop()
            if token == "+": stack.append(v1 + v2)
            elif token == "-": stack.append(v2 - v1)
            elif token == "*": stack.append(v1 * v2)
            elif token == "/": stack.append(int((v2 * 1.0) / v1))
        return stack[0] # 4. return last digit in stack

"""
.isalnum() - check alphanumerical
.isalpha() - check alphabetical
.isdigit() - check if digit excludes < 0
"""