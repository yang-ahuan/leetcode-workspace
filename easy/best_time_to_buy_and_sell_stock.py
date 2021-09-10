# Idea : I optimize the brute method. I record maximum price in the future and decrese the time of looking for maxmum number.
# Time/space complexity : O(n^2) / O(1)
# Status : Time limit exceeded (208/211)
# Bottleneck : When prices list is descending, this method is equal to brute method
class Solution:
    def maxProfit(self, prices: list) -> int:
        max_number = max(prices)
        best_profit = 0
        for first_day_idx in range(len(prices)-1):
            if max_number == prices[first_day_idx]:
                max_number = max(prices[first_day_idx+1:])
            profit = max_number - prices[first_day_idx]
            if profit > best_profit:
                best_profit = profit
        return best_profit

# Idea : This idea is just the opposite, recording minimum price in the past. While scanning prices list, calculate maxmum profit.
# Time/space complexity : O(n) / O(1)
class Solution:
    def maxProfit(self, prices: list) -> int:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit