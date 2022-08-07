""" 
* 在空间复杂度是 O(MN) 的解法中, 也就是 s1, 我们需要对于每个出现的 0 都修改对应的行列。那么, 如果「同一个行（列）」中出现了「两个 0」, 则需要把该行（列）置「两遍 0」 。无论是空间还是时间复杂度, 都不好。
* 一个容易得到的方法是：第一次遍历矩阵, 记录一下每行、列是否出现了 0; 如果出现了 0, 进行记录, 然后在第二次遍历时将此行列置为 0。

/ 用 O(m+n)额外空间
? https://leetcode.cn/problems/set-matrix-zeroes/solution/xiang-jie-ge-chong-kong-jian-fu-za-du-de-y4pd/
"""


class Solution(object):
    def setZeroes(self, matrix):
        zeroRowSet = set()
        zeroColSet = set()

        numRows = len(matrix)
        numCols = len(matrix[0])
        # * 第一遍遍历matrix, 并用集合记录哪些行,哪些列有 0
        for i in range(numRows):
            for j in range(numCols):
                if matrix[i][j] == 0:
                    zeroRowSet.add(i)
                    zeroColSet.add(j)

        # * 第二遍遍历matrix, 根据两个set, 进行置 0 操作
        for i in range(numRows):
            for j in range(numCols):
                if i in zeroRowSet or j in zeroColSet:
                    matrix[i][j] = 0
