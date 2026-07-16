from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        fresh = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        if fresh == 0:
            return 0
        
        while q and fresh != 0:
            for _ in range(len(q)):#very important
                r,c = q.popleft()
                for dr,dc in directions:
                    nr = r+dr
                    nc = c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        fresh-=1
                        q.append((nr,nc))
                        grid[nr][nc] = 2
            time += 1
        if fresh != 0:
            return -1
        else:
            return time







