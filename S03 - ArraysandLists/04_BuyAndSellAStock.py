class Solution(object):
    """
    Compute the maximum profit from one buy/sell stock transaction.
    """

    def maxProfit(self, prices):
        """
        Return the largest possible profit from buying once and selling once.
        """
        result = 0                 # best profit found
        minValue = prices[0]       # lowest price seen so far

        for i in range(1, len(prices)):
            if prices[i] < minValue:
                minValue = prices[i]          # update minimum price
            else:
                profit = prices[i] - minValue # profit if sold today
                if profit > result:
                    result = profit           # update best profit

        return result

# instantiate and test
s = Solution()

print(s.maxProfit([7,1,5,3,6,4]))       # 5
print(s.maxProfit([7,6,4,3,1]))         # 0
print(s.maxProfit([2,4,1]))             # 2
