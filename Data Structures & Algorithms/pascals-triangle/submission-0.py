class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        if n == 2:
            return [[1],[1,1]]
        
        res = [[1],[1,1]]

        for i in range(2,n):
            row = [1]

            for j in range(i-1):
                row.append(res[i-1][j] + res[i-1][j+1])
            
            row.append(1)
            res.append(row)
        return res