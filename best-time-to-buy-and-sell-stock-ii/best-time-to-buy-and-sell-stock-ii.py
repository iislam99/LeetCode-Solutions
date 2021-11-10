class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = 0
        max = 0
        index = 0
        profit = 0
        
        while index < len(prices) - 1:
            while index < len(prices) - 1 and prices[index] >= prices[index + 1]:
                index += 1
            min = prices[index]
            
            while index < len(prices) - 1 and prices[index] <= prices[index + 1]:
                index += 1
            max = prices[index]
            
            profit += max - min
        
        return profit