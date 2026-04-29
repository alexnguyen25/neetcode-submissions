class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [[1, 0], [0,1], [-1,0], [0,-1]]

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == "0":
                return
            else:
                grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r+dr, c+dc)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        return islands
        