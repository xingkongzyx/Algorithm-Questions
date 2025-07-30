""" 
? 题目可视化: https://leetcode.cn/problems/coloring-a-border/solution/1034bian-jie-zhao-se-ti-mu-ke-shi-hua-by-m47v/ 

? 思路: https://leetcode.cn/problems/coloring-a-border/solution/1034-bian-jie-zhao-se-qu-yu-sheng-chang-11t4l/

? 代码借鉴: https://leetcode.cn/problems/coloring-a-border/solution/chun-c-dfs-by-haoyangong-vfsr/

/时间复杂度: O(mn), 其中 m 和 n 分别是 grid 的行数和列数。在最坏情况下, 我们需要访问两边 grid。    
/空间复杂度: O(mn)。递归栈可能存储了 grid 每一个节点
"""


class Solution(object):
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """

        # * 上下左右
        dir_x = [-1, 1, 0, 0]
        dir_y = [0, 0, -1, 1]
        originColor = grid[row][col]
        numRows = len(grid)
        numCols = len(grid[0])

        def inArea(x, y):
            return 0 <= x < numRows and 0 <= y < numCols

        # 用一个特殊值（-1）在 visited 数组中表示 "边界", 其余搜过的标记为1, 未搜过的默认是0；
        visited = [[0 for _ in range(numCols)] for _ in range(numRows)]

        # 返回值用来表示当前网格是否出界(1.矩阵之外 或 2.颜色不同). false 代表「出界」了
        def DFS(rowIdx, colIdx):
            if inArea(rowIdx, colIdx) == False:
                return False

            if grid[rowIdx][colIdx] != originColor:
                return False

            if visited[rowIdx][colIdx] != 0:
                return True

            visited[rowIdx][colIdx] = 1
            for i in range(4):
                newRow = rowIdx + dir_x[i]
                newCol = colIdx + dir_y[i]
                directionCheck = DFS(newRow, newCol)
                # print(f"for current cell({rowIdx}, {colIdx}), its neightbor {newRow}, {newCol} returns {directionCheck}")

                # * 只要当前格子的上下左右任何一个方向的 neighbor cell 是「越界的」或者是「a square not in the component」, DFS 就会返回 false. 只要有 false, 说明「当前格子 grid[rowIdx][colIdx]」 是border, 需要「染色」, 这里将对应的 visited 数组中的位置记录为 -1
                if directionCheck == False:
                    visited[rowIdx][colIdx] = -1

            return True

        DFS(row, col)

        for row in range(numRows):
            for col in range(numCols):
                if visited[row][col] == -1:
                    grid[row][col] = color

        return grid
