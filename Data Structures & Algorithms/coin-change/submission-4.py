class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0

        for coin in coins:
            for amt in range(1,amount+1):
                if coin<=amt:
                    dp[amt] = min(dp[amt],dp[amt-coin]+1)

        if dp[-1] == float("inf"):
            return -1
        else:
            return dp[-1]