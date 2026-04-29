class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        length = 1
        if grid[0][0] == 0:
            queue.append((0,0))
            visited.add((0,0))
        else:
            return -1

        while queue:
            for i in range(len(queue)):
                directions = [[0,1], [1,0], [-1,0], [0,-1], [1,1], [-1,-1], [1,-1], [-1, 1]]
                r, c = queue.popleft()
                for dr, dc in directions:
                    if(min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols or grid[r+dr][c+dc] == 1 or (r+dr, c+dc) in visited):
                        continue
                    queue.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))
                    if r+dr == rows-1 and c+dc ==cols - 1:
                        return length + 1
            length += 1
        if (rows - 1, cols - 1) in visited:
            return length
        else:
            return -1
            





        