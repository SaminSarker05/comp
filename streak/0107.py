class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        # n^2 solution works
        res = set()

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j: continue
                if words[j] in words[i]:
                    res.add(words[j])
                    break

        return list(res)


        # helper function to check if substring; can also just use in keyword

        def helper(s1, s2):
            if len(s1) < len(s2):
                return False

            for i in range(len(s1)):
                if s1[i] == s2[0]:
                    if i + len(s2) <= len(s1) and s1[i:i+len(s2)] == s2:
                        return True
            
            return False
        res = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if j == i: continue
                if helper(words[i], words[j]):
                    res.add(words[j])
        
        return list(res)



        
