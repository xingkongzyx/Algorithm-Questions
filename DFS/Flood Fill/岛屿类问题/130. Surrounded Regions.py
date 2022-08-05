""" 
「」〖〗²《》〔〕『』
* 题目中解释说「被包围的区间」不会存在于边界上, 所以我们会想到边界上的 O 要特殊处理, 只要把边界上的 O 特殊处理了, 那么剩下的 O 替换成 X 就可以了。问题转化为, 如何寻找「和边界联通」的 O, 我们需要考虑如下情况。
* 从边界出发, 对图进行 dfs, 从而寻找「和边界联通」的 O, 并将其替换为 @, 待第一次 dfs 搜索结束之后, 进行第二次普通的全图遍历, 此时遇到的 O 都是「和边界不联通」的 O, 需要将其替换为 X; 遇到的 @, 则要重新变回 O (因为 @ 的前身是和边界连通的 O)。 

? https://leetcode.cn/problems/surrounded-regions/solution/bfsdi-gui-dfsfei-di-gui-dfsbing-cha-ji-by-ac_pipe/
/ 时间复杂度: O(rows * cols), 其中 rows 和 cols 分别为矩阵的行数和列数, 深度优先遍历过程中, 每一个单元格至多只会被标记一次；第二次遍历时, 每个单元格又被经过一次
/ 空间复杂度: O(rows * cols), 深度优先遍历最多使用的栈的开销为整个棋盘的大小。

"""


class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        numRows = len(board)
        numCols = len(board[0])
        # first dfs all points in 4 sides to change all boarder Os to @, change all inner Os to X, and all @s to Os
        # * 把四周有 O 的地方都替换成为 @, 在四周进行 DFS 遍历；

        def firstTraverse(rowIdx, colIdx):
            # print(rowIdx, colIdx)
            if inArea(rowIdx, colIdx) == False or board[rowIdx][colIdx] != "O":
                return

            # * 把数组中的 O 变成 @，意思是这个 O 和边缘是连通的
            board[rowIdx][colIdx] = "@"
            # *  之后从当前坐标开始上下左右进行递归搜索
            firstTraverse(rowIdx + 1, colIdx)
            firstTraverse(rowIdx - 1, colIdx)
            firstTraverse(rowIdx, colIdx + 1)
            firstTraverse(rowIdx, colIdx - 1)

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        # * 搜索第一列和最后一列
        for i in range(numCols):
            if board[0][i] == "O":
                firstTraverse(0, i)
            if board[numRows - 1][i] == "O":
                firstTraverse(numRows - 1, i)

        # * 搜索第一行和最后一行
        for j in range(numRows):
            if board[j][0] == "O":
                firstTraverse(j, 0)
            if board[j][numCols - 1] == "O":
                firstTraverse(j, numCols - 1)

        # * 再从头到尾遍历一遍, 把 O 换成 X, 把 @ 换成 O。
        for rowIdx in range(numRows):
            for colIdx in range(numCols):
                if board[rowIdx][colIdx] == "O":
                    board[rowIdx][colIdx] = "X"
                elif board[rowIdx][colIdx] == "@":
                    board[rowIdx][colIdx] = "O"
        # print(board)
        return board
