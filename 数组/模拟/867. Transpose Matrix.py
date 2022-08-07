""" 
* Transpose Matrix 就是把 M 行 N 列的矩阵，转成 N 行 M 列的矩阵，原来矩阵中 matrix[i][j] 的位置，会交换到新矩阵的 res[j][i] 位置。

? https://leetcode.cn/problems/transpose-matrix/solution/zhuan-zhi-ju-zhen-de-san-chong-yu-yan-da-l7ye/
/ Time Complexity: O(n*m), where n is the row and m is the column
/ Space Complexity: O(n*m)
"""


class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        result = [[None for _ in range(num_rows)] for _ in range(num_cols)]

        # * 原来矩阵中 matrix[i][j] 的位置，会交换到新矩阵的 res[j][i] 位置。
        for i in range(num_rows):
            for j in range(num_cols):
                result[j][i] = matrix[i][j]

        return result
