class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 0. get row col values
        m = len(board)
        n = len(board[0])

        # 1. dfs algo to start from border and mark all compromised Os that cant be captured
        def traverse(i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = '$' # protect the point on board to indicate compromised
                traverse(i + 1, j)
                traverse(i - 1, j)
                traverse(i, j + 1)
                traverse(i, j - 1)

        # 2. loop through border and all points with O
        for i in range(m):
            if board[i][0] == 'O': traverse(i, 0)
            if board[i][n-1] == 'O': traverse(i, n-1)
        for j in range(n):
            if board[0][j] == 'O': traverse(0, j)
            if board[m-1][j] == 'O': traverse(m-1, j)

        # 3. after dfs flip all valid Os and revert the protected
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                elif board[i][j] == '$': board[i][j] = 'O'