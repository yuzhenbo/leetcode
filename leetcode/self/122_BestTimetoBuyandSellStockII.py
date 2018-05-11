class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = 0

        if not prices:
            return 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                diff += prices[i] - prices[i-1]
        return diff
