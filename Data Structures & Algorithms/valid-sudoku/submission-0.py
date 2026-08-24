class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    if num in cols[i] or num in rows[j] or num in boxes[(i//3)+(j//3)*3]:
                        return False
                    cols[i].add(num)
                    rows[j].add(num)
                    boxes[(i//3)+(j//3)*3].add(num)
        return True
