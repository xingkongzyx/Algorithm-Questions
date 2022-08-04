""" 
## 还是运用岛屿的模板代码, 求周长重要的是细化内部的终止条件。
# ➀ 从一个岛屿方格走向网格边界, 周长加 1。
# ➁ 从一个岛屿方格走向水域方格, 周长加 1。
# ➂ 从一个岛屿方格走向已经遍历过的陆地, 周长加 0, 因为已经遍历过的格子不对周长做任何贡献
* 为什么呢? 从土地到土地，之间不会产生周长，但从土地迈入海洋，之间会产生 1 个周长，从土地迈出矩阵边界，也会产生 1 个周长。
? https://leetcode.cn/problems/island-perimeter/solution/shou-hua-tu-jie-463-dao-yu-de-zhou-chang-by-xiao_b/
/ 时间复杂度: O(nm), 其中 n 为网格的高度, m 为网格的宽度。每个格子至多会被遍历一次, 因此总时间复杂度为 O(nm)。
/ 空间复杂度: O(nm)。深度优先搜索复杂度取决于递归的栈空间, 而栈空间最坏情况下会达到 O(nm)。

"""


class Solution(object):
    def islandPerimeter(self, grid):
        for rowIdx in range(0, len(grid)):
            for colIdx in range(0, len(grid[0])):
                if(grid[rowIdx][colIdx] == 1):
                    return self.dfs(grid, rowIdx, colIdx)

    # * DFS 从一个点，向四周扩散，目标是遇到矩阵边界或海水，它们是答案已知的 base case，是位于递归树底部的 case，是递归的终止条件。
    def dfs(self, grid, row, col):
        if(not self.inArea(grid, row, col)):
            return 1
        if(grid[row][col] == 0):
            return 1
        if(grid[row][col] == 2):
            return 0
        grid[row][col] = 2

        #! 对于当前遍历到的格子, 不用像求最大面积时将各个方向 dfs 计算出的周长和的结果再加上本格子的 1, 自己这个格子贡献的边长是通过向各个方向进行 DFS 得到结果。如果这个格子上面就是超出边界, 那么当继续向上dfs时, 上面的格子会直接返回1.
        leftIslandsPerimeter = self.dfs(grid, row, col-1)
        rightIslandsPerimeter = self.dfs(grid, row, col+1)
        topIslandsPerimeter = self.dfs(grid, row - 1, col)
        bottomIslandsPerimeter = self.dfs(grid, row + 1, col)

        return leftIslandsPerimeter + rightIslandsPerimeter + topIslandsPerimeter + bottomIslandsPerimeter

    def inArea(self, grid, row, col):
        if(row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])):
            return True
        else:
            return False
