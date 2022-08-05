""" 
* 把输入的「原始数组」复制一份(注意需要 deep copy), 然后遍历「拷贝数组」判断某个位置是否为 0, 如果是 0, 说明「原始数组」中的该位置就是0。那么直接修改「原始数组」这个位置对应的行和列为 0, 但是「拷贝数组」在整个过程中都不会进行任何修改，用作参考。
/ 时间复杂度: O(MN*(M+N))
/ 空间复杂度: O(MN)
#? https://leetcode.cn/problems/set-matrix-zeroes/solution/xiang-jie-ge-chong-kong-jian-fu-za-du-de-y4pd/ 
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        import copy
        matrixCopy = copy.deepcopy(matrix)
        numRows = len(matrix)
        numCols = len(matrix[0])

        for rowIdx in range(numRows):
            for colIdx in range(numCols):
                if matrixCopy[rowIdx][colIdx] == 0:
                    # change the row whose idx is rowIdx to 0
                    for cIdx in range(numCols):
                        matrix[rowIdx][cIdx] = 0

                    # change the col whose idx is colIdx to 0
                    for rIdx in range(numRows):
                        matrix[rIdx][colIdx] = 0
