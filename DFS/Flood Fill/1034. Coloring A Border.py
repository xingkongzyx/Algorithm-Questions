""" 
? 题目可视化: https://leetcode.cn/problems/coloring-a-border/solution/1034bian-jie-zhao-se-ti-mu-ke-shi-hua-by-m47v/ 

* 首先通过 DFS 遍历标记所有属于 "connected component" 的节点为「特殊色 -1」, 代表这个节点「被访问过」并且属于 "connected component". 等四周递归完成后，进行边界判断，以及恢复不是边界的节点的颜色。判断的方法是: 检查「当前节点」的上下左右四个节点是否都为 -1 或者是否都为「旧颜色」, 是的话说明当前节点属于 "connected component" 但同时又不属于 "border of a connected component", 将其恢复成「旧颜色」. 
# 正因为有「恢复」的操作，所以上面判断标准是 -1 或者「旧颜色」. 如果当前节点的「相邻」四个节点都不属于 boarder, 并且在前面的递归过程中已经被恢复成了「旧颜色」, 这种情况下, 当前节点同样满足「恢复」颜色的条件.
* 最后再遍历一遍 grid, 将所有为 「特殊色 -1」 的位置换成「目标色」, 因为这些位置就是题目所求的 "border of a connected component"

/时间复杂度: O(mn), 其中 m 和 n 分别是 grid 的行数和列数。在最坏情况下, 我们需要访问两边 grid。    
/空间复杂度: O(mn)。递归栈可能存储了 grid 每一个节点
? 代码参考: https://leetcode.cn/problems/coloring-a-border/solution/1034-bian-kuang-zhao-se-by-jnpeng945-ppxh/

"""


class Solution(object):
    def colorBorder(self, grid, row, col, color):
        numRows = len(grid)
        numCols = len(grid[0])
        oldColor = grid[row][col]

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        def traverse(rowIdx, colIdx):
            if inArea(rowIdx, colIdx) == False:
                return

            if grid[rowIdx][colIdx] != oldColor:
                return

            grid[rowIdx][colIdx] = -1
            traverse(rowIdx + 1, colIdx)
            traverse(rowIdx - 1, colIdx)
            traverse(rowIdx, colIdx + 1)
            traverse(rowIdx, colIdx - 1)
            candidates = [-1, oldColor]
            # * 如果当前节点不是 "border of a connected component", 则将其恢复成「旧颜色」.
            if 0 < rowIdx < numRows - 1 \
                    and 0 < colIdx < numCols - 1 \
                    and grid[rowIdx-1][colIdx] in candidates \
                    and grid[rowIdx+1][colIdx] in candidates \
                    and grid[rowIdx][colIdx - 1] in candidates \
                    and grid[rowIdx][colIdx + 1] in candidates:
                grid[rowIdx][colIdx] = oldColor

        traverse(row, col)
        #* 第二次遍历
        for rowIdx in range(numRows):
            for colIdx in range(numCols):
                if grid[rowIdx][colIdx] == -1:
                    grid[rowIdx][colIdx] = color

        return grid


grid = [
    [2, 1, 3, 2, 1, 1, 2],
    [1, 2, 3, 1, 2, 1, 2],
    [1, 2, 1, 2, 2, 2, 2],
    [2, 1, 2, 2, 2, 2, 2],
    [2, 3, 3, 3, 2, 1, 2]
]
Solution().colorBorder(grid, 4, 4, 3)
""" 
[
    [2,1,3,2,1,1,2],
    [1,2,3,1,2,1,2],
    [1,2,1,2,2,2,2],
    [2,1,2,2,2,2,2],
    [2,3,3,3,2,1,2]
]
[[2, 1, 3, 2, 1, 1, -1], 
[1, 2, 3, 1, -1, 1, -1], 
[1, 2, 1, -1, 2, -1, -1],
[2, 1, -1, -1, -1, -1, -1], 
[2, 3, 3, 3, -1, 1, -1]]
"""
