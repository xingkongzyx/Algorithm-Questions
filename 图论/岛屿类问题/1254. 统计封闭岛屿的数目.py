'''
#! 这题要求封闭的岛屿数，所谓封闭岛屿换个角度看就是不能接触到二维数组边界的岛屿。所以可以在dfs中返回是否接触了边界。如果没有接触边界，则这一次dfs遍历找到一个封闭岛屿。
#* 我是直接通过dfs的返回值来记录是否接触了边界，如果返回true则到达边界。这里需要注意的细节是上下左右四个方向都要遍历到，不能因为某个方向返回true了就直接退出，特别注意的是不能用 || 连接4个dfs递归调用，否则可能被短路掉就不对了。当然还有一种做法是在dfs中增加一个引用参数，传出是否到达边界（或是否是封闭）。

#? https://leetcode.cn/problems/number-of-closed-islands/solution/dian-xing-dao-yu-ti-dfsjie-ti-xi-jie-by-happyfire/

在遍历过程中如果遇见陆地就进行 dfs 遍历，但如果这个遍历会遍历到grid之外，这一块遍历的陆地不算做封闭陆地，我们return False. 只有四周全是水，才说明是封闭陆地

#/ 时间复杂度 O(m*n)　其中 m，n 是 grid 的行数和列数
#/ 空间复杂度 O(m*n)

'''


class Solution:
    # 0 （土地）和 1 （水）组成
    def closedIsland(self, grid):
        res = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == 0:
                    checkRes = self.dfs(grid, row, col)
                    if(checkRes == True):
                        res += 1
        return res

    def dfs(self, grid, row, col):
        if not self.inArea(grid, row, col):
            return False
        if(grid[row][col] != 0):
            return True
        grid[row][col] = 2

        topcheck = self.dfs(grid, row - 1, col)
        bottomcheck = self.dfs(grid, row + 1, col)
        rightcheck = self.dfs(grid, row, col + 1)
        leftcheck = self.dfs(grid, row, col - 1)
        # 类似于二叉树中的后序遍历，把这块陆地的四周都遍历完，看看是否有不封闭的方向，有的话返回false，否则返回true
        if topcheck == False or bottomcheck == False or rightcheck == False or leftcheck == False:
            return False
        return True

    def inArea(self, grid, row, col):
        if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
            return True

    def printGrid(self, grid):
        for row in grid:
            print(row, "\n")
        print("-----------------------------------------\n")


grid = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],

        [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],

        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],

        [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],

        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]]
s = Solution()
res = s.closedIsland(grid)
print(res)
