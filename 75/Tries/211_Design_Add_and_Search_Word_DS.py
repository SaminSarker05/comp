class WordDictionary(object):

    def __init__(self):
        self.words = {}

    def addWord(self, word):
 
        store = self.words
        for char in word:
            if char not in store:
                store[char] = {}
            store = store[char]

        store['-'] = None
        

    def search(self, word):
        def find(store, word):
            if not store:
                return False
            if not word:
                return '-' in store
            if word[0] == '.':
                for sub in store:
                    if find(store[sub], word[1:]):
                        return True
                return False

            if word[0] in store:
                return find(store[word[0]], word[1:])
            
            return False

        return find(self.words, word)



