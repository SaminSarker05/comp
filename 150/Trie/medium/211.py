# 0. created TrieNode data structure to represent words and their end
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_last = False


class WordDictionary(object):
    def __init__(self):
        # 1. initialise root TrieNode
        self.root = TrieNode()

    # 2. add pathway to TrieNode tree and mark ending
    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_last = True

    # 3. recursive function in case a . encountered
    def search(self, word):
        def helper(node, word):
            curr = node
            for i in range(len(word)):
                # 4. if . then make recursive call with all possible next characters
                if word[i] == '.': 
                    for n in curr.children:
                        if helper(curr.children[n], word[i+1:]): return True
                    return False
                if word[i] not in curr.children: return False
                curr = curr.children[word[i]]
            
            return curr.is_last
        return helper(self.root, word)