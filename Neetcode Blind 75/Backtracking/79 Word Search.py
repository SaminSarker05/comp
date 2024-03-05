class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution(object):
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        root = TrieNode()

        cursor = root
        for char in word:
            if char not in cursor.children:
                cursor.children[char] = TrieNode()
            cursor = cursor.children[char]
        cursor.is_word = True

        def search(i, j, node):
            if node.is_word:
                return True

            if 0 <= i < m and 0 <= j < n and board[i][j] in node.children:
                c = board[i][j]
                new_node = node.children[c]
                board[i][j] = "#"
                u = search(i+1, j, new_node)
                d = search(i-1, j, new_node)
                l = search(i, j+1, new_node)
                r = search(i, j-1, new_node)
                board[i][j] = c
                return u or d or l or r
            
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and search(i, j, root):
                    return True
            
        return False
