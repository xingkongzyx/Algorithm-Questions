'''
#* 这题求「封闭」的岛屿数, 所谓「封闭岛屿」换个角度看就是这座岛屿是否接触到「二维数组边界」之外。
#* 在遍历过程中如果遇见「陆地」就进行 DFS 遍历, 如果这个遍历会遍历到 grid 之外, 这一块遍历的「陆地」不算做「封闭岛屿」, 我们 return False. 只有四周全是水, 才说明是「封闭岛屿」
#* 这里需要注意的细节是上下左右「四个方向」〖都要遍历〗到, 不能因为某个方向返回True 了就直接退出, 特别注意的是不能用 || 连接 4 个 DFS 递归调用, 否则可能被短路掉就不对了。
## 非常重要: 当我们选择了一个「陆地」, 我们就必须要把该「陆地」所在的岛屿上的所有「陆地」位置遍历完, 如果没遍历完就结束, 就相当于把一块岛屿分成了几个小块岛屿, 如果原先的这块岛屿是封闭岛屿, 这样遍历就可能会得到几块封闭岛屿。得到的结果是大于答案的。

#? https://leetcode.cn/problems/number-of-closed-islands/solution/dian-xing-dao-yu-ti-dfsjie-ti-xi-jie-by-happyfire/
#? https://leetcode.cn/problems/number-of-closed-islands/solution/yi-ti-kan-tou-dfs-he-dfs-by-xiao-xiao-suan-fa/

#/ 时间复杂度 O(m*n) 其中 m, n 是 grid 的行数和列数
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
        # * 从当前陆地开始出发, 如果能走出边界就说明该陆地所在岛屿不是封闭岛屿, 返回 False
        if self.inArea(grid, row, col) == False:
            return False
        # * 如果碰到水域(值为 1 的点)或者已经遍历过的的陆地(值为 2 的点)就返回 True, 表示这个方向满足「封闭岛屿」的要求
        if(grid[row][col] != 0):
            return True

        # * 如果碰到陆地(值为 0 的点)就继续向该陆地的四个方向遍历, 同时将该陆地标记为 2, 表示这个位置已经遍历过了。DFS代码如下
        grid[row][col] = 2

        top_check = self.dfs(grid, row - 1, col)
        bottom_check = self.dfs(grid, row + 1, col)
        right_check = self.dfs(grid, row, col + 1)
        left_check = self.dfs(grid, row, col - 1)

        return top_check and bottom_check and right_check and left_check

    def inArea(self, grid, rowIdx, colIdx):
        return 0 <= rowIdx < len(grid) and 0 <= colIdx < len(grid[0])

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
