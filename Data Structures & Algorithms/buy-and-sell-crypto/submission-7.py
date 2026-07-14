class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 1:
            return 0

        left = 0
        right = 1

        temp = ans = 0

        while right<n:
            if prices[left]<prices[right]:
                temp = prices[right]-prices[left]
                ans = max(ans,temp)
            else:
                left = right
            right += 1 #very important
        return ans