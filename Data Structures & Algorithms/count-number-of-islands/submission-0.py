class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        for i, row in enumerate(grid):
            for j, cel in enumerate(grid[i]):
                if cel == "1":
                    cnt += 1
                    self.propagate_from(grid, i, j)
                    print(grid)

        return cnt

    def propagate_from(self, grid, i, j):
        if not (0 <= i < len(grid)):
            return
        if not (0 <= j < len(grid[i])):
            return

        if grid[i][j] == "1":
            grid[i][j] = "x"

        if 0 <= i+1 < len(grid) and grid[i+1][j] == "1":
            self.propagate_from(grid, i+1, j)
        if 0 <= i-1 < len(grid) and grid[i-1][j] == "1":
            self.propagate_from(grid, i-1, j)
        if 0 <= j+1 < len(grid[i]) and grid[i][j+1] == "1":
            self.propagate_from(grid, i, j+1)
        if 0 <= j-1 < len(grid[i]) and grid[i][j-1] == "1":
            self.propagate_from(grid, i, j-1)
