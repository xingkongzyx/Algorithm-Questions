""" 
* 注释版的代码在下面的评论中

/ 时间复杂度: O(1) move() 只需判断四个值是否等于 n
/ 空间复杂度: 只保存行/列/对角线的和, 而不用保存所有元素, 空间复杂度从O(n²)降到O(n)
? https://leetcode.cn/problems/design-tic-tac-toe/solution/python-o1shi-jian-onkong-jian-jie-ti-si-lu-by-ljbu/
"""


class TicTacToe:

    def __init__(self, n: int):
        # *  一共有两个 players, 每个player都有一个用于记录自己的每一行的和的数组(一共是 n 行, 所以总的大小是 2 * n)
        self.rowSum = [[0 for _ in range(n)] for _ in range(2)]
        # *  一共有两个 players, 每个player都有一个用于记录自己的每一列的和的数组(一共是 n 列, 所以总的大小是 2 * n)
        self.colSum = [[0 for _ in range(n)] for _ in range(2)]
        # *  一共有两个对角线的方向, 分别是「左上=>右下」, 以及「左下=>右上」。每个player都有两个用于记录自己的每一种对角线和的位置, 也就是下面两个变量的由来。
        # * 下面数组代表『player1 的「左上=>右下」的对角线的和』, 以及『player2 的「左上=>右下」的对角线的和』
        self.diagonalLRSum = [0, 0]
        self.diagonalRLSum = [0, 0]
        self.goal = n

    def move(self, row: int, col: int, player: int) -> int:
        playerIdx = player - 1
        # * 对应 player 的其行的和与列的和都加 1
        self.rowSum[playerIdx][row] += 1
        self.colSum[playerIdx][col] += 1
        # * 如果当前点在对角线上, 这个玩家对应的两条对角线的和也加 1
        if row == col:
            self.diagonalLRSum[playerIdx] += 1
        if row + col == self.goal - 1:
            self.diagonalRLSum[playerIdx] += 1

        # * 如果「上下左右」或者「对角线」有一种情况满足要求, 就说明当前 player 是获胜者
        if self.rowSum[playerIdx][row] == self.goal \
                or self.colSum[playerIdx][col] == self.goal \
                or self.diagonalLRSum[playerIdx] == self.goal \
                or self.diagonalRLSum[playerIdx] == self.goal:
            return player

        return 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
