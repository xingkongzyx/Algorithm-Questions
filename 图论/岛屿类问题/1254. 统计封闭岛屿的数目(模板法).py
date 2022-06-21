'''
首选去除与岸边相连的岛屿，然后按照「岛屿数量」的思路计算
时间复杂度：O(mn)。其中 m、n 分别为矩阵的行数和列数。
空间复杂度：O(mn)。递归所需要的栈空间大小为 m、n 。

'''


class Solution:
    def closedIsland(self, grid):
        # 将与岸边相连的上下两边的陆地变为 数字2，代表因为不完全封闭不再考虑的陆地
        for i in range(len(grid[0])):
            if grid[0][i] == 0:
                self.dfs(grid, 0, i)
            if grid[len(grid) - 1][i] == 0:
                self.dfs(grid, len(grid) - 1, i)
        # 将与岸边相连的左右两边的陆地变为 数字2，代表因为不完全封闭不再考虑的陆地
        for i in range(0, len(grid)):
            if grid[i][0] == 0:
                self.dfs(grid, i, 0)
            if grid[i][len(grid[0]) - 1] == 0:
                self.dfs(grid, i, len(grid[0]) - 1)
        res = 0

        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                if grid[row][col] == 0:
                    self.dfs(grid, row, col)
                    res += 1
        return res

    def dfs(self, grid, row, col):
        if not self.inArea(grid, row, col):
            return
        if(grid[row][col] != 0):
            return
        grid[row][col] = 2
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)

    def inArea(self, grid, row, col):
        if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
            return True


grid = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]
print(grid)
s = Solution()
res = s.closedIsland(grid)
print(res)
