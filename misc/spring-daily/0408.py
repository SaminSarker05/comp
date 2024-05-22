class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        time = 0
        # 1. simulate line passing by decrementing everyone still needing ticket
        while tickets[k] != 0:
            # 2. loop through people who require ticket and increment time
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    time += 1
                    tickets[i] -= 1
                    # 3. if person at k becomes 0 end loop early 
                    if i == k and tickets[k] == 0:
                        break
        return time
