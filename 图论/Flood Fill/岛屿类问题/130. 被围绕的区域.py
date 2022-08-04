""" 
根据题意： 四个边的 O 以及与其相邻的 O 都无法被 X 包围 ，因此，可以先把四周的 O 以及 O 的连通分量全部变成 'N'（一个与 O 和 X 不同的字符即可）。然后再把内部的O 按要求变成 X, 最后再遍历一次棋盘，把 "N" 恢复成 O。

时间复杂度：O(rows * cols)，其中 rows 和 cols 分别为矩阵的行数和列数，深度优先遍历过程中，每一个单元格至多只会被标记一次；
空间复杂度：O(rows * cols)，深度优先遍历最多使用的栈的开销为整个棋盘的大小。

"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for colIdx in range(0, len(board[0])):
            if(board[0][colIdx] == "O"):
                self.firstTimeDFS(board, 0, colIdx)
            if(board[len(board) - 1][colIdx] == "O"):
                self.firstTimeDFS(board, len(board) - 1, colIdx)
        for rowIdx in range(0, len(board)):
            if(board[rowIdx][0] == "O"):
                self.firstTimeDFS(board, rowIdx, 0)
            if(board[rowIdx][len(board[0]) - 1] == "O"):
                self.firstTimeDFS(board, rowIdx, len(board[0]) - 1)

        # self.printGrid(board)
        for i in range(1, len(board)):
            for j in range(1, len(board[0])):
                if board[i][j] == "O":
                    self.secondTimeDFS(board, i, j)
        # self.printGrid(board)
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == "N":
                    board[i][j] = "O"
        # self.printGrid(board)

    def firstTimeDFS(self, grid, r, c):
        if(not self.inArea(grid, r, c)):
            return

        if(grid[r][c] != 'O'):
            return
        grid[r][c] = "N"
        self.firstTimeDFS(grid, r + 1, c)
        self.firstTimeDFS(grid, r - 1, c)
        self.firstTimeDFS(grid, r, c + 1)
        self.firstTimeDFS(grid, r, c - 1)

    def secondTimeDFS(self, grid, r, c):
        if(not self.inArea(grid, r, c)):
            return

        if(grid[r][c] != 'O'):
            return
        grid[r][c] = "X"
        self.secondTimeDFS(grid, r + 1, c)
        self.secondTimeDFS(grid, r - 1, c)
        self.secondTimeDFS(grid, r, c + 1)
        self.secondTimeDFS(grid, r, c - 1)

    def inArea(self, grid, r, c):
        return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[0])

    def printGrid(self, grid):
        for row in grid:
            print(row, "\n")
        print("-----------------------------------------\n")


board = [["X"]]
s = Solution()
res = s.solve(board)
print(res)
