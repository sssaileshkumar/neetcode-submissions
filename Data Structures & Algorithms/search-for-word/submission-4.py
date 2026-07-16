class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(r,c,i):
            if i == len(word): 
                return True
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c] != word[i] or board[r][c] == "visited":
                return False
            
            temp = board[r][c]
            board[r][c] = "visited"

            res = backtrack(r+1,c,i+1) or backtrack(r-1,c,i+1) or backtrack(r,c+1,i+1) or backtrack(r,c-1,i+1)

            board[r][c] = temp
            return res
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(i,j,0) == True:
                    return True
        return False