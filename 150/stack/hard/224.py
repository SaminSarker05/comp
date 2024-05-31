class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 0. recursive solution; pass in index; solve subproblems denoted by ()
        def helper(index):
            # 1. hold total, digit, and sign of current problem
            total, digit, sign = 0, 0, 1
            while index < len(s):
                # 2. if digit then calculate running digit
                if s[index].isdigit(): digit = digit * 10 + int(s[index])
                # 3. if operand than update total considering sign and update sign and reset digit
                elif s[index] in '+-':
                    total += digit * sign
                    digit = 0
                    sign = 1 if s[index] == "+" else -1
                # 4. if ( then make recursive call; add returned ans with sign
                elif s[index] == '(':
                    subprob, index = helper(index + 1)
                    total += subprob * sign
                # 5. if ) make return call for sub problem with current index
                elif s[index] == ')':
                    total += digit * sign
                    return total, index
                index += 1 # 6. continue while valid index in s
            # 5. return total + digit and consider sign
            return total + digit * sign

        return helper(0)      