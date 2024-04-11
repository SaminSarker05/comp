class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        # 1. base cases
        if len(num) == 0 or len(num) == k: return "0"
        
        # 2. building a monotonic stack
        stack = []
        for n in num:
            # 3. remove element when no longer monotonic
            while stack and k and n < stack[-1]:
                k -= 1
                stack.pop()
            # 4. dont add leading zeroes
            if stack or n != "0":
                stack.append(n)
        
        # 5. if only monotonic then just delete k rightmost elements
        if k: stack = stack[:-k]

        return "0" if not stack else "".join(stack)
        
        