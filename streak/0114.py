class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # loop through A and B and add each number to a dictionary
        # key must exist in both to be considered in prefix common array

        dict_a = defaultdict(int)
        dict_b = defaultdict(int)

        set_a = set()
        set_b = set()
        seen = set()
        res = []

        for i in range(len(A)):
            set_a.add(A[i]) # use hashset instead of hashmap since frequency don't matter
            set_b.add(B[i])
            t = 0
            # if same number then prefix common only increases by 1
            if A[i] == B[i]: 
                t += 1
            else:   # otherwise check if each number exists in other
                if A[i] in set_b: t += 1
                if B[i] in set_a: t += 1

            if res: 
                res.append(res[-1] + t)
            else: 
                res.append(t)

            # SLOWER
            # t = 0
            # update the frequency of each number; don
            # dict_a[A[i]] += 1
            # dict_b[B[i]] += 1
            # seen.add(A[i])
            # seen.add(B[i])
            # t = 0
            # # don't need to loop through all keys
            # for char in seen:
            #     t += min(dict_a[char], dict_b[char])

            # res.append(t)
        
        return res







        
