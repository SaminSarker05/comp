class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """

        # 0. create prefix tree of words
        root = TrieNode()
        for word in dictionary:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.is_word = True
        
        # 1. split dictionary into seperate words
        words = sentence.split(" ")
        res = ""

        # 2. loop through each word to find its root
        for word in words:
            path = ""
            curr = root
            flag = True
            for char in word:
                # 3. if root does not exist then just add word
                if char not in curr.children: break
                curr = curr.children[char]
                path += char
                # 4. if end of word then add to res
                if curr.is_word:
                    res += path + " "
                    break
            # 5. add remaining word or if word not in prefix tree
            if curr.is_word == False:
                res += word + " "
            
        return res[:-1]
