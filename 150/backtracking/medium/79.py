class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution(object):
    def exist(self, board, word):

        m = len(board)
        n = len(board[0])

        # 0. set up prefix tree to hold word
        curr = root = TrieNode()
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        # 1. mark end of word
        curr.is_word = True
        
        # 2. dfs algo to search word in board
        def dfs(i, j, node):
            # 3. if end of word then return True since found
            if node.is_word: return True
            if 0 <= i < m and 0 <= j < n and board[i][j] in node.children:
                char = board[i][j]
                next_node = node.children[board[i][j]]
                # 4. use placeholder to not repeat index
                board[i][j] = "#"
                u = dfs(i + 1, j, next_node)
                d = dfs(i - 1, j, next_node)
                l = dfs(i, j + 1, next_node)
                r = dfs(i, j - 1, next_node)
                board[i][j] = char

                return u or d or l or r
            return False

        # 4. traverse through board start if first letter match
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, root): return True
        
        return False