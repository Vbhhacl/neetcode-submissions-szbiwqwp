class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = prices
        n = len(price)
        profit =[0]
        for i in range (0,n-1):
            buy_value = price[i]
            for j in range (i,n):
                sell_value = price[j]
                if (sell_value>=buy_value):
                    p = sell_value - buy_value
                    profit.append(p)
        return max(profit)