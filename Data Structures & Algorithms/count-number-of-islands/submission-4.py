class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [[1, 0], [0,1], [-1,0], [0,-1]]
        visited = set()
        queue = deque()


        def bfs(r, c):
            if(r < 0 or c < 0 or c == cols or r == rows or grid[r][c] == "0"):
                return
            else:
                queue.append((r,c))
                grid[r][c] = "0"
            while queue:
                for i in range(len(queue)):
                    rop, cop = queue.popleft()
                    for dr, dc in directions:
                        bfs(rop +dr,cop+dc)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1
        return islands
        