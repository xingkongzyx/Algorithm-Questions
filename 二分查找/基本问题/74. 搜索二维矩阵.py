""" 
! 用 240. 的写法也能AC, 时间复杂度是 O(N + M)
? https://leetcode.cn/problems/search-a-2d-matrix/solution/fu-xue-ming-zhu-liu-chong-fang-fa-bang-n-e20z/
"""


class Solution:
    def searchMatrix(self, matrix, target):
        rowIdx = 0
        colIdx = len(matrix[0]) - 1

        while rowIdx < len(matrix) and colIdx >= 0:
            # * 从矩阵的右上角开始匹配，如果匹配到了，返回true
            if matrix[rowIdx][colIdx] == target:
                return True
            # * 如果值比target大，说明这一列都比target大，column往左移一行
            elif matrix[rowIdx][colIdx] > target:
                colIdx -= 1
            # * 如果值比target小，则说明这一行都比target小，row往下移一行
            else:
                rowIdx += 1

        return False
