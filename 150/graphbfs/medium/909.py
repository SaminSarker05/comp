class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        # BFS algo, store square and number of moves in deque
        n = len(board)
        q = deque()
        q.append((1, 0))

        def findcoors(current_position):
            # 0. calculate row col using division and modulo
            row = n - 1 - (current_position - 1) // n 
            col = (current_position - 1) % n    
            # 1. since swapping left right order check this condition               
            if row % 2 == n % 2: return (row, n - 1 - col)
            else: return (row, col)
        
        seen = set()
        while q:
            curr, moves = q.popleft()
            # 1. if end of game reached return # of moves
            if curr == n * n: return moves 
            # 2. choose next square from [1, 6]
            for i in range(1, 7):
                # 3. if sqaure outside of board stop
                if curr + i > (n * n): break
                # 4. find associated row col on board
                row, col = findcoors(curr + i)

                # 6. do not reapeat a move
                if (row, col) not in seen:
                    seen.add((row, col))

                    # 7. if board is a snake or ladder use corresponding value
                    if board[row][col] != -1:
                        q.append((board[row][col], moves + 1))
                    else: q.append((curr + i, moves + 1))
            
        return -1