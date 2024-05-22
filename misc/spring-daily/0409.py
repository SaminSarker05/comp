class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        
        # 1. to get solution reverse operations of simulation
        deck.sort(reverse=True)
        res = deque()

        # 2. if stuff in deque pop from right and add to left
        for card in deck:
            if res:
                res.appendleft(res.pop())
            res.appendleft(card)
        
        return res


        # 1. base cases return sorted deck 
        if len(deck) == 1: return deck
        if len(deck) == 2: return sorted(deck)

        # 2. sort deck in increasing order
        deck.sort()
        # 3. use indexes to place cards in right order
        res = [0] * len(deck)
        d = deque(range(len(deck)))

        # 4. loop through cards and place at right index using simulation decscribed
        for c in deck:
            res[d.popleft()] = c
            if d:
                d.append(d.popleft())
        
        return res
