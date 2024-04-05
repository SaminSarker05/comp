class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1. use stack to keep track of valid chars
        stack = []

        for char in s:
            # 2. if stack nonempty and meets case requirments remove top and dont add
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            # 3. otherwise add char to stack
            else:
                stack.append(char)
        
        return ''.join(stack)

        