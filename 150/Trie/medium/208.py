# TRIENODE: USES INCLUDE AUTOCOMPLETE and SPELL CHECK (PREFIX TREE)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                # 0. adding new pathway in Trie PREFIX Tree
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        # 1. mark end of work in TREE
        curr.is_end = True
    
    def search(self, word: str) -> bool:
        curr = self.root
        # 2. look for word by following paths in tree
        for char in word:
            if char not in curr.children: return False
            # 3. if next character exists follow that path by redefining TrieNode
            curr = curr.children[char]
        # 4. looking for word so ensure end of word found
        return curr.is_end
 
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        # 5. same procedure as search but word ending does not matter
        for char in prefix:
            if char not in curr.children: return False
            curr = curr.children[char]
        return True
   
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)