class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        # storing mapping in vertex using index is faster


        # 1. store mapping of those trusted and peoples votes
        candidates = defaultdict(list)
        people = {i:[] for i in range(1, n+1)}

        # 2. add each edge relation to maps
        for n1, n2 in trust:
            candidates[n2].append(n1)
            people[n1].append(n2)
        
        # 3. only found judge when trusts no one and is trusted by everyone
        for k, v in people.items():
            if len(v) == 0:
                if len(candidates[k]) == len(people) - 1:
                    return k
        
        return -1


            