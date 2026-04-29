class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [[1, 0], [0,1], [-1,0], [0,-1]]


        def dfs(r, c):
            queue = deque()
            visited = set()
            queue.append((r, c))
            grid[r][c] = "0"
            while queue:
                for i in range(len(queue)):
                    nr, nc = queue.popleft()
                    for dr, dc in directions:
                        if nr + dr < 0 or nr + dr == rows or nc + dc < 0 or nc + dc == cols or grid[nr+dr][nc+dc] == "0":
                            continue
                        else:
                            queue.append((nr+dr, nc+dc))
                            grid[nr+dr][nc+dc] = "0"


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        return islands
        