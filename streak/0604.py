class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        # 0. make hashtable for letter frequency of first word
        letters = defaultdict(int)
        for char in words[0]: letters[char] += 1

        # 1. traverse through rest of words
        for word in words[1:]:
            # 2. make temp hashtable for word freq
            temp = defaultdict(int)
            for char in word: temp[char] += 1

            # 3. update the common frequency table to be the min of curr and word tables
            for char, val in letters.items():
                letters[char] = min(val, temp[char])
        
        # 4. add to res the letter * its common count across words
        res = []
        for key, val in letters.items():
            for i in range(val): res.append(key)

        return res
