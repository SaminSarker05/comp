class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """

        # 0. make bank into set for faster lookup
        valid = set(bank)

        # 1. store seen gene sequences to not repeat calculations
        seen = set()

        # 2. use BFS algo using deque
        q = deque()
        q.append((startGene, 0))
        seen.add(startGene)

        while q:
            # 3. if gene == endgine return # of moves
            gene, moves = q.popleft()
            if gene == endGene: return moves
            # 4. loop through each possible character and update a letter in the gene
            for val in ("A", "C", "G", "T"):
                for i in range(len(gene)):
                    possible = gene[:i] + val + gene[i+1:]
                    # 5. if this sequence exists in bank and wasnt seen before then add to queue and seen
                    if possible not in seen and possible in valid: 
                        seen.add(possible)
                        q.append((possible, moves + 1))
        
        return -1