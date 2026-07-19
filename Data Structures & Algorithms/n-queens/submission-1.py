class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for _ in range(n)]

        cols = set()
        posDiag = set()
        negDiag = set()

        def backtrack(row):
            if row == n:
                res.append(["".join(row) for row in board])
                return
            for col in range(n):
                if col not in cols and row+col not in posDiag and row-col not in negDiag:
                    board[row][col] = "Q"
                    cols.add(col)
                    posDiag.add(row+col)
                    negDiag.add(row-col)
                
                    backtrack(row+1)

                    board[row][col] = "."
                    cols.remove(col)
                    posDiag.remove(row+col)
                    negDiag.remove(row-col)
            return res
        return backtrack(0)