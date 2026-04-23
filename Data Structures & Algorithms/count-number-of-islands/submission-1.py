class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(x,y):
            grid[x][y] = '0'
            dirs = [(1,0),(-1,0),(0,-1),(0,1)]
            for dx, dy in dirs:
                if 0<=x+dx<ROWS and 0<=y+dy<COLS and grid[x+dx][y+dy] == '1':
                    dfs(x+dx,y+dy)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res