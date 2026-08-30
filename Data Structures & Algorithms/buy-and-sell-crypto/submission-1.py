class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        ans = 0
        left = 0
        right = 1

        while left<len(prices) and right<len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                ans = max(ans,profit)
                right += 1
            else:
                left = right
                right += 1
        return ans