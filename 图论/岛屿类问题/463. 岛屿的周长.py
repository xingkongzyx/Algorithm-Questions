""" 
## 还是运用岛屿的模板代码，这次因为求周长，所以经过要细化内部的终止条件。如果因为超出边界，则返回1；如果因为周边的格子是海洋，则返回1；如果因为旁边格子是已经遍历过的陆地，则返回0，因为已经遍历过的格子不对周长做任何贡献

时间复杂度：O(nm)，其中 nn 为网格的高度，mm 为网格的宽度。每个格子至多会被遍历一次，因此总时间复杂度为 O(nm)。

空间复杂度：O(nm)。深度优先搜索复杂度取决于递归的栈空间，而栈空间最坏情况下会达到 O(nm)。

"""


class Solution(object):
    def islandPerimeter(self, grid):
        for rowIdx in range(0, len(grid)):
            for colIdx in range(0, len(grid[0])):
                if(grid[rowIdx][colIdx] == 1):
                    return self.dfs(grid, rowIdx, colIdx)

    def dfs(self, grid, row, col):
        if(not self.inArea(grid, row, col)):
            return 1
        if(grid[row][col] == 0):
            return 1
        if(grid[row][col] == 2):
            return 0
        grid[row][col] = 2
        #! 这个格子自己不用像求最大面积时 将各个边dfs算出的和再加上自己的1，自己这个格子贡献的边长通过向各个方向进行dfs得到结果。如果这个格子上面就是超出边界，那么当继续向上dfs时，上面的格子会直接返回1.
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


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
s = Solution()
res = s.islandPerimeter(grid)
print(res)
