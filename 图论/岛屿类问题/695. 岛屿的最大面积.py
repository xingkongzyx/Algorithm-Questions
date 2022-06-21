""" 
? 时间复杂度：O(m×n)。其中 m 是给定网格中的行数，n 是列数。我们访问每个网格最多一次。
? 空间复杂度：O(m×n)，递归的深度最大可能是整个网格的大小，因此最大可能使用 O(m×n) 的栈空间。

https://leetcode.cn/problems/max-area-of-island/solution/fang-ge-lei-dfs-de-jian-dan-fang-fa-cjava-by-nette/

 """


class Solution:
    def maxAreaOfIsland(self, grid):
        # / 定义一个表示岛屿的最大面积
        area = 0
        # /这个两层for循环是用来遍历整张二维表格中所有的陆地(也就是grid[row][col]为1的陆地)
        # /其中 rowIdx 表示行，colIdx 表示列
        for rowIdx in range(0, len(grid)):
            for colIdx in range(0, len(grid[0])):
                if(grid[rowIdx][colIdx] == 1):
                    currentIslandArea = self.dfs(grid, rowIdx, colIdx)
                    area = max(area, currentIslandArea)
        return area

    def dfs(self, grid, r, c):
        # / 判断 base case
        # / 如果坐标(r, c) 超出了网格范围，返回面积0
        if(not self.inArea(grid, r, c)):
            return 0
        # / 访问上、下、左、右四个相邻结点

        # /如果这个格子不是陆地或者这个格子是已经被访问过的陆地，则直接返回面积0
        if(grid[r][c] != 1):
            return 0

        # / 将当前是陆地的格子标记为「已遍历过」
        grid[r][c] = 2
        # ! 计算从当前格子起步前后左右相邻土地的面积，相当于二叉树遍历中计算左右子树返回的结果
        bottomIslandArea = self.dfs(grid, r + 1, c)
        topIslandArea = self.dfs(grid, r - 1, c)
        rightIslandArea = self.dfs(grid, r, c + 1)
        leftIslandArea = self.dfs(grid, r, c - 1)
        # ! + 1 是加上当前格子的面积
        return 1 + bottomIslandArea + topIslandArea + rightIslandArea + leftIslandArea

    # / 判断坐标(r, c) 是否在网格中
    def inArea(self, grid, r, c):
        return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[0])


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

s = Solution()
res = s.maxAreaOfIsland(grid)
print(res)
