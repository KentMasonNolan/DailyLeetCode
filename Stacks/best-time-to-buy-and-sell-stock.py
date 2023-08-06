class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        left, right = 0,1

        maxProfit = 0

        for i in range(len(prices)):
            currentProfit = prices[right] - prices[left]
            if currentProfit > maxProfit:

