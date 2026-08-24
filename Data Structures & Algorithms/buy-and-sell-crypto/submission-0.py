class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        ans = 0

        while right<len(prices):
            if prices[right] > prices[left]:
                temp = prices[right] - prices[left]
                ans = max(ans,temp)
            else:
                left = right
            right += 1
        
        return ans