""" 
* 这道题的规则如何简化？
* 1. 原来是活的, 周围有2-3个活的, 成为活的
* 2. 原来是死的, 周围有3个活的, 成为活的
* 3. 其他都是死了
* 解法: 复制一份原始数组；根据复制数组中邻居细胞的状态来更新 board 中的细胞状态。
? 底下评论区有更优解法: https://leetcode.cn/problems/game-of-life/solution/sheng-ming-you-xi-by-leetcode-solution/
? https://leetcode.cn/problems/game-of-life/solution/ju-zhen-wen-ti-tong-yong-jie-fa-by-freshrookie/
"""


class Solution:

    def gameOfLife(self, board) -> None:
        import copy

        # this copy is used to changed and returned
        cloned_copy = copy.deepcopy(board)
        dir_arr = [[-1, -1], [-1, 0], [-1, 1],
                   [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        numRows = len(board)
        numCols = len(board[0])

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        for rowIdx in range(numRows):
            for colIdx in range(numCols):
                # * 对于每一个细胞统计其八个相邻位置里的活细胞数量
                liveCells = 0
                for x_offset, y_offset in dir_arr:
                    newRowIdx = rowIdx + x_offset
                    newColIdx = colIdx + y_offset
                    if inArea(newRowIdx, newColIdx) and cloned_copy[newRowIdx][newColIdx] == 1:
                        liveCells += 1

                # * if current cell is live, and then apply with the rule
                if cloned_copy[rowIdx][colIdx] == 1:
                    if liveCells < 2:
                        board[rowIdx][colIdx] = 0
                    elif liveCells > 3:
                        board[rowIdx][colIdx] = 0
                # * if current cell is dead, and then apply with the rule
                elif cloned_copy[rowIdx][colIdx] == 0:
                    if liveCells == 3:
                        board[rowIdx][colIdx] = 1
