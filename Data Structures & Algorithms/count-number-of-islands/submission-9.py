class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        n_of_islands = 0
        visited_islands = set()

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            visited_islands.add((r, c))

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (
                        nr >= ROWS or nc >= COLS or
                        nr < 0 or nc < 0 or
                        grid[nr][nc] == '0' or
                        (nr, nc) in visited_islands
                    ):
                        continue

                    queue.append((nr, nc))
                    visited_islands.add((nr, nc))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited_islands:
                    bfs(row, col)
                    n_of_islands += 1

        return n_of_islands