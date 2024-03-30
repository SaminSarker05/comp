class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1: return 0

        profit = 0
        buy = prices[0]

        for r in range(1, len(prices)):
            # 1. minimize buy prices 
            if buy > prices[r]:
                # 2. if smaller buy price found they update
                buy = prices[r]
            # 3. maximize profit 
            profit = max(profit, prices[r]-buy)
        
        return profit