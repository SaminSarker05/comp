class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        cursor = self
        for letter in word:
            if letter not in cursor.children:
                cursor.children[letter] = TrieNode()
            cursor = cursor.children[letter]
        cursor.is_word = True


class Solution(object):
    def findWords(self, board, words):
        root = TrieNode()
        ROWS, COLS = len(board), len(board[0])

        for word in words: root.add_word(word)

        def search(i, j, node, path):
            if node.is_word:
                res.add(path)
                node.is_word = False

            if i < 0 or i == ROWS or j < 0 or j == COLS: return
            c = board[i][j]
            if board[i][j] not in node.children: return
            
            path += c
            next_node = node.children[c]
            board[i][j] = "#"
            search(i+1, j, next_node, path)
            search(i-1, j, next_node, path)
            search(i, j+1, next_node, path)
            search(i, j-1, next_node, path)
            board[i][j] = c

        res, seen = set(), set()
        for i in range(ROWS):
            for j in range(COLS):
                search(i, j, root, "")

        return res