""" 
? 思路参考: https://leetcode.cn/problems/rotate-image/solution/48-xuan-zhuan-tu-xiang-chao-jian-ji-yi-d-nuau/
? 外国 https://leetcode.com/problems/rotate-image/solutions/18879/ac-java-in-place-solution-with-explanation-easy-to-understand/?orderBy=most_votes 

* 上下对称: matrix[i][j] ➩ matrix[n-i-1][j] (列不变)
* 左右对称: matrix[i][j] ➩ matrix[i][n-j-1] (行不变)
* 主对角线对称: matrix[i][j] ➩ matrix[j][i] (行列互换)
* 副对角线对称: matrix[i][j] ➩ matrix[n-j-1][n-i-1] (行列均变, 且互换)

* 那么, 对于顺时针 90° 旋转, 即本题, 先写出转移式: 
* matrix[i][j] ➩ matrix[j][n-i-1], 
* 可以观察到, 我们希望原来的列 j 不变, 且要交换行列位置。
* 因此可以分解为: 主对角线对称 + 左右对称, 
! 注意分解顺序是不能换的。
# 主对角线对称: matrix[i][j] ➩ matrix[j][i] 
# 左右对称(也就是代码中的以「中心」的竖线为轴做翻转): matrix[j][i] ➩ matrix[j][n-1-i]
? 各来自种旋转角度非常好的总结: https://leetcode.cn/problems/rotate-image/solution/lu-qing-ge-chong-by-pennx-ce3x/
/ 时间复杂度: O(N^2) 其中 N 是 matrix 的边长。对于每一次翻转操作，我们都需要枚举矩阵中一半的元素。
/ 额外空间: O(1) 为原地翻转得到的原地旋转。
"""


class Solution(object):
    def rotate(self, matrix):
        numRows = len(matrix)
        numCols = len(matrix[0])
        # * 先以「左上-右下」对角线为轴做翻转,
        for rowIdx in range(numRows):
            for colIdx in range(rowIdx):
                matrix[rowIdx][colIdx], matrix[colIdx][rowIdx] = matrix[colIdx][rowIdx], matrix[rowIdx][colIdx]

        # * 再以「中心」的竖线为轴做翻转
        midIdx = numCols // 2
        for rowIdx in range(numRows):
            for colIdx in range(midIdx):
                temp = matrix[rowIdx][numCols - 1 - colIdx]
                matrix[rowIdx][numCols - 1 - colIdx] = matrix[rowIdx][colIdx]
                matrix[rowIdx][colIdx] = temp

        return matrix


Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
