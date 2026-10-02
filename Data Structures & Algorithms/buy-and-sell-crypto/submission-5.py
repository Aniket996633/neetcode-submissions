class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_p:
                min_p = price
            elif price - min_p > max_profit:
                max_profit = price - min_p
        return max_profit