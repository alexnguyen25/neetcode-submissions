class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        length = 1
        directions = [[0,1], [1,0], [-1,0], [0,-1], [1,1], [-1,-1], [1,-1], [-1, 1]]

        if grid[0][0] == 0:
            queue.append((0, 0))
            visited.add((0,0))
        else:
            return -1
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols -1:
                    return length
                for dr, dc in directions:
                    if r+dr < 0 or c+dc <0 or r+dr == rows or c+dc == cols or grid[r+dr][c+dc] == 1 or (r+dr, c+dc) in visited:
                        continue
                    else:
                        queue.append((r+dr, c+dc))
                        visited.add((r+dr,c+dc))
            length+= 1
        
        if (rows - 1, cols-1) in visited:
            return length
        else:
            return -1
                        

        