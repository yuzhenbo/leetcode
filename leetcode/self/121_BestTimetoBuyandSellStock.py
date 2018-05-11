class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not  prices:
            return 0
        low = max(prices)
        max_fit = 0
        for i in range(1,len(prices)):
            low = min(low, prices[i-1])
            profit = prices[i] - low
            max_fit = max(max_fit, profit)
        return max_fit

