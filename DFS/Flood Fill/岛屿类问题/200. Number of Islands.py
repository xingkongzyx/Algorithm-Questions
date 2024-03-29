""" 
/ DFS为什么要沉岛
/ 遍历遇到 1 即遇到土地, 土地肯定在一个岛上, 计数 +1
/ 如果不把与它和同在一个岛的土地变成 0, 则DFS遍历到它们时, 会对一个岛重复计数
? 来自: https://leetcode.cn/problems/number-of-islands/solution/tong-ji-wan-yi-ge-dao-hou-yao-ba-ta-chen-liao-200-/
? https://leetcode.cn/problems/number-of-islands/solution/by-lfool-2wmw/
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir_x = [0, 0, 1, -1]
        dir_y = [1, -1, 0, 0]
        # / 定义一个表示岛屿数量的变量
        count = 0
        # / 这个两层for循环是用来遍历整张二维表格中所有的陆地(也就是grid[row][col]为1的陆地)
        # / 其中 rowIdx 表示行, colIdx 表示列
        for rowIdx in range(len(grid)):
            for colIdx in range(len(grid[0])):
                if(grid[rowIdx][colIdx] == "1"):
                    self.dfs(grid, rowIdx, colIdx, dir_x, dir_y)
                    count += 1
        return count

    def dfs(self, grid, r, c, dir_x, dir_y):
        # / 终止条件：
        # / ➀ 坐标(r, c) 超出了网格范围;
        if(not self.inArea(grid, r, c)):
            return

        # / ➁ 如果这个格子不是陆地或者这个格子是已经被访问过的陆地, 则直接返回
        if(grid[r][c] != '1'):
            return

        # / 访问上、下、左、右四个相邻结点
        # / 将当前是陆地的格子标记为「已遍历过」
        grid[r][c] = "2"

        for i in range(4):
            new_r = r + dir_x[i]
            new_c = c + dir_y[i]
            self.dfs(grid, new_r, new_c, dir_x, dir_y)

    # / 判断坐标(r, c) 是否在网格中

    def inArea(self, grid, r, c):
        return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[0])
