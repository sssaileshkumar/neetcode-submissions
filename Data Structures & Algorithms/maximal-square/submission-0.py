class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = []
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            dp.append(row)

        for i in range(rows):
            dp[i][0] = int(matrix[i][0])
        
        for i in range(cols):
            dp[0][i] = int(matrix[0][i])
        
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(
                                dp[i-1][j],dp[i][j-1],dp[i-1][j-1]
                            )+1
        
        ans = 0

        for i in range(rows):
            for j in range(cols):
                ans = max(ans,dp[i][j])
        return ans*ans