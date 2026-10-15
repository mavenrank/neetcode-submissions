class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        best_profit=0
        cheapest_seen=prices[0]
        for i in range(len(prices)):
            if prices[i]<cheapest_seen:
                cheapest_seen=prices[i]
            else:
                current_profit = prices[i]-cheapest_seen
                if current_profit > best_profit:
                    best_profit=current_profit
        return best_profit