class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_len = len(words[0])
        word_str = len(words) * word_len
        res = []
        for pos in range(word_len):
            i = posz
            # counter is a dict subclass
            d = Counter(words) # dict for words required
            for j in range(i, len(s) + 1 - word_len, word_len):
                word = s[j: j + word_len]
                d[word] -= 1 # decrement requirements 
                while d[word] < 0: # if found to many need to slide window
                    d[s[i: i : word_len]] += 1
                    i += word_len
                if i + word_str == j + word_len:
                    res.append(i)
        return res

"""

- use sliding window and hashmap
- check if all words were met
"""
