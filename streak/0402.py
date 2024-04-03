class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution(object):
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        
        # 1. trienode use to replace hashset use
        root = TrieNode()
        curr = root
        
        # 2. make a mapping using dicts of the word
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

        def dfs(i, j, node):
            # 3. use trieNode to check if word was found
            if node.is_word:
                return True
            if i >= 0 and i < m and j >= 0 and j < n and board[i][j] in node.children:
                val = board[i][j]
                # 4. set and later reset location value to prevent reuse
                board[i][j] = "#"
                # 5. change node to be next letter
                u = dfs(i+1, j, node.children[val])
                d = dfs(i-1, j, node.children[val])
                l = dfs(i, j+1, node.children[val])
                r = dfs(i, j-1, node.children[val])
                
                board[i][j] = val

                return u or d or l or r
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, root):
                    return True
        return False



        m = len(board)
        n = len(board[0])
        seen = set()

        # 1. depth first search
        def dfs(i, j, string, pos):
            if string == word:
                return True
            # 2. if valid indices, coordinate not seen, and equal to expected char
            if i >= 0 and i < m and j >= 0 and j < n and (i,j) not in seen and board[i][j] == word[pos]:
                seen.add((i, j))
                string += board[i][j]
                t = dfs(i+1, j, string, pos+1)
                d = dfs(i-1, j, string, pos+1)
                l = dfs(i, j+1, string, pos+1)
                r = dfs(i, j-1, string, pos+1)
                # 3. remove seen so can be used again
                seen.remove((i, j))
            
                return t or d or l or r
            
            return False
                
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, "", 0):
                    return True
        
        return False



        