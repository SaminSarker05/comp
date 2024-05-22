class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1. store string in array to change values at index
        string = [c for c in s]
        stack = []
        # 2. use for loop to erase extra right paren
        for i, val in enumerate(s):
            if val == '(':
                # 3. store index in stack
                stack.append(i)
            elif val == ')' and stack:
                stack.pop()
            elif val == ')':
                string[i] = ''

        # 4. delete extra left paren 
        while stack:
            string[stack.pop()] = ''

        return ''.join(string)   
