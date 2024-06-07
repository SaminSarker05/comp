class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # 0. make wordlist into set for faster lookup
        bank = set(wordList)
        # 1. base case
        if endWord not in wordList: return 0

        # 2. bfs algo using deque
        q = deque()
        q.append((beginWord, 0))
        seen = set()
        seen.add(beginWord)

        while q:
            word, moves = q.popleft()
            # 3. if endword found return number of words required
            if word == endWord: return moves + 1
            for i in range(len(word)):
                # 4. loop through each character and make possible word with letter in alphabet
                for char in range(97, 123):
                    possible = word[:i] + chr(char) + word[i+1:]
                    # 5. if new word and word in bank then add to deque
                    if possible not in seen and possible in bank:
                        q.append((possible, moves + 1))
                        seen.add(possible)

        return 0