# 0. trieNode implementation to store words to be found
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
class Solution(object):
    def findWords(self, board, words):
        # 1. initialize Trie prefix tree root
        root = TrieNode()

        # 2. add all words to tree
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.is_end = True
        
        m = len(board)
        n = len(board[0])
        res = set()
        seen = set()
        
        # 3. DFS algo to check if path to word exists
        def dfs(i, j, path, node):
            if node.is_end: 
                res.add(path)
                # 4. if a word found add to res and make into possible prefix
                node.is_end = False

            if 0 <= i < m and 0 <= j < n and (i, j) not in seen and board[i][j] in node.children:
                seen.add((i, j))
                path += board[i][j]
                next_TrieNode = node.children[board[i][j]]
                dfs(i + 1, j, path, next_TrieNode)
                dfs(i - 1, j, path, next_TrieNode)
                dfs(i, j - 1, path, next_TrieNode)
                dfs(i, j + 1, path, next_TrieNode)
                seen.remove((i, j))
        
        # 5. loop through all char in board looking for words
        for i in range(m):
            for j in range(n):
                dfs(i, j, "", root)
        
        return res