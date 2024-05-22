'''
time complexity: O(n) 
space complexity: O(1)
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 1:
            return 0
        
        # calculate profit based on curr and min
        # calculate min based on min and curr

        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - buy)
            buy = min(buy, prices[i])
        return profit