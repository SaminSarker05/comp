class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # prefix sum 

        # base case
        if len(s) < 3: return 0
        
        seen = set()
        uniq = set()
        mapp = {}

        prefix_uniq = [] # track # of unique elements seen thus far in array
        for i in range(len(s)):
            uniq.add(s[i])
            prefix_uniq.append(len(uniq))
        
        # track the rightmost position of an element if it repeats
        prefix_seen = [-1 for i in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            if s[i] in mapp: 
                prefix_seen[i] = mapp[s[i]]
            else: 
                mapp[s[i]] = i

        res = 0
        for i in range(len(s)):
            # since only length 3; we need identical left and right chars
            loc = prefix_seen[i]
            if loc == -1 or s[i] in seen: continue
            # if a identical char exists on right; use right most char 
            seen.add(s[i])
            word = s[i + 1:loc]
            # need # of unique letters between two duplicates; since middle letter can be anything
            res += len(set(word))   # was overdoing it; this works

        return res
