""" 
? https://leetcode.cn/problems/range-sum-query-2d-immutable/solutions/629187/ru-he-qiu-er-wei-de-qian-zhui-he-yi-ji-y-6c21/?orderBy=most_votes
? https://leetcode.cn/problems/range-sum-query-2d-immutable/solutions/629163/er-wei-qian-zhui-he-jian-dan-tui-dao-tu-sqekv/?orderBy=most_votes
/ 时间复杂度: 预处理前缀和数组需要对原数组进行线性扫描, 复杂度为 O(n*m), 计算结果复杂度为 O(1)。整体复杂度为 O(n*m)
/ 空间复杂度: O(n * m)


"""


class NumMatrix:
    def __init__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        self.preSum = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                self.preSum[i + 1][j + 1] = (
                    self.preSum[i][j + 1]
                    + self.preSum[i + 1][j]
                    - self.preSum[i][j]
                    + matrix[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        return (
            self.preSum[row2 + 1][col2 + 1]
            - self.preSum[row2 + 1][col1]
            - self.preSum[row1][col2 + 1]
            + self.preSum[row1][col1]
        )
