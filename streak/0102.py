class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # prefix sum

        # prefix count of words that end and start with vowel
        prefix = []
        vowels = set(['a', 'e', 'i', 'o', 'u']) # hashset for quick check if vowel
        running = 0
        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                running += 1
            prefix.append(running)
        
        # process queries and use prefix sum for quick calculation
        res = []
        for a, b in queries:
            if a == 0:
                res.append(prefix[b])
            else:
                res.append(prefix[b] - prefix[a - 1])
            
        return res
