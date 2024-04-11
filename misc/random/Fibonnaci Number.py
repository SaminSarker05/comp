class Solution(object):
    def fib(self, n):
        # store fib sequence in an array
        # use memoization and dp

        array = [None] * (n+1)

        if n == 0:
            return 0

        def helper(n, array):
            if n == 1 or n == 2:
                return 1
            if array[n] != None:
                return array[n]
            else:
                result = helper(n-1, array) + helper(n-2, array)
            array[n] = result
            return result
        
        return helper(n, array)