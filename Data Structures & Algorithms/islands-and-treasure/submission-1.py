class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        time = 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 2147483647):
                        grid[row][col] = time
                        q.append((row, col))
            time += 1
        return