class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        large=0
        buy=prices[0]
        n=len(prices)
        for i in range (n):
            if prices[i]>buy:
                large=max(large,prices[i]-buy)
            buy=min(buy,prices[i])
        return large
