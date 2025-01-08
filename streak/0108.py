class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        # easy problem; brute force method works; built in python methods
        res = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len(words[j]) >= len(words[i]):
                    # python methods string.startswith(str), string.endswith(str)
                    if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                        res += 1
                    # if words[j][:len(words[i])] == words[i] and words[j][-len(words[i]):] == words[i]:
                    #     res += 1
        
        return res
