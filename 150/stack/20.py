class Solution(object):
    def isValid(self, s):
        # 0. use stack to ensure valid order LIFO order
        stack = []

        # 1. use dict to hold pair match in reverse order
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            # 2. if end character found check for pair match
            if char == "]" or char == ")" or char == "}":
                if not stack or stack[-1] != mapping[char]: return False
                else: stack.pop()  # 3. if match then remove pair
            else: stack.append(char)
        return len(stack) == 0  # 4. stack itself must be empty to denote all pair completion
            