class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 0. sets to track captured squares
        cols = set()
        diags = set()
        antidiags = set()

        # 1. dfs algo to find all possible solutions
        def dfs(row):
            # 2. if index of row outside board then a solution has been found
            if row == n: return 1
            res = 0
            # 3. loop through cols and see if a queen can be placed
            for col in range(n):
                # 4. if valid square place queen add update sets
                if not(col in cols or row-col in diags or row+col in antidiags):
                    cols.add(col)
                    diags.add(row-col)
                    antidiags.add(row+col)
                    # 5. make recursive call from next row
                    res += dfs(row+1)

                    # 6. remove from sets to allow backtracking
                    cols.remove(col)
                    diags.remove(row-col)
                    antidiags.remove(row+col)

            return res
        
        return dfs(0)




        