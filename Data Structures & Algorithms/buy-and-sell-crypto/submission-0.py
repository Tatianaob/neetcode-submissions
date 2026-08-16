class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # [10,1,5,6,7,1]
        # max profit = 6   
        # price at 1 is the best to buy then sell it at 7 : 7-1 = 6 profit

    # two pointers
    # left the day we buy
    # right the day we sell
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP



        