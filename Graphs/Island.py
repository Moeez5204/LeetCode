class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        NO_islands = 0
        Lenght = len(grid)
        Height = len(grid[0])

        def dfs(row, col):
            if row < 0 or row == Lenght or col < 0 or col == Height:
                return

            if grid[row][col] != '1':
                return

            grid[row][col] = 'Visited'

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for row in range(Lenght):
            for col in range(Height):
                if grid[row][col] == '1':
                    dfs(row, col)
                    NO_islands += 1

        return NO_islands



