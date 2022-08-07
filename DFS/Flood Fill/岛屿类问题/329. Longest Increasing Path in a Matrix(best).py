""" 
* 深度优先搜索是非常直观的方法。从一个单元格开始进行「深度优先搜索」, 即可找到从该单元格开始的『最长递增路径』。对每个单元格分别进行「深度优先搜索」之后, 即可得到矩阵中的『最长递增路径』的长度。〖但是〗, 如果使用朴素深度优先搜索, 时间复杂度是指数级, 会超出时间限制, 因此必须加以优化。
* 因此可以使用『记忆化』的方法进行优化。用矩阵 memo 作为缓存矩阵, 已经计算过的单元格的结果存储到缓存矩阵中。使用记忆化深度优先搜索, 当访问到一个单元格 (i,j) 时, 如果 memo[i][j] != -1, 说明该单元格的结果已经计算过, 则直接从缓存中读取结果, 如果 memo[i][j] == -1, 说明该单元格的结果尚未被计算过, 则进行搜索, 并将计算得到的结果存入缓存中。

# 为什么不像其他岛屿类题目一样使用 visited 数组, 也没有改变已经访问过的位置的元素?
* 因为在内循环里, "matrix[newRowIdx][newColIdx] > matrix[rowIdx][colIdx]" 确保了之前已经访问过的元素根本就不会出现在后续的路径里, 所以 visited 就没有存在的意义,。或者说题目中要求是搜索元素递增的最长深度，所以元素递增可以作为元素是否被访问的标志，
? 参考: https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/solution/ju-zhen-zhong-de-zui-chang-di-zeng-lu-jing-by-le-2/512498

? 关于记忆化的讲解: https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/solution/c-ju-zhen-zhong-de-zui-chang-di-zeng-lu-jing-ji-yi/

/ 时间复杂度: O(m*n). m是行数, n是列数, 矩阵元素遍历了一遍
/ 空间复杂度 O(m*n)
"""


class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        x_dir = [0, 0, 1, -1]
        y_dir = [1, -1, 0, 0]

        numRows = len(matrix)
        numCols = len(matrix[0])

        def traverse(rowIdx, colIdx, memo):
            # *  return if result is already calculated
            if memo[rowIdx][colIdx] != -1:
                return memo[rowIdx][colIdx]

            # * curLen 初始为1因为我们有起始点本身就算一个长度
            curLen = 1
            # * choosing each possible move available to us
            for i in range(4):
                newRowIdx = rowIdx + x_dir[i]
                newColIdx = colIdx + y_dir[i]
                # * bound checking as well as move to next cell only when it is greater in value
                if inArea(newRowIdx, newColIdx) and matrix[newRowIdx][newColIdx] > matrix[rowIdx][colIdx]:
                    directionLen = 1 + traverse(newRowIdx, newColIdx, memo)
                    curLen = max(curLen, directionLen)

            memo[rowIdx][colIdx] = curLen
            return curLen

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols
        # * memo[i][j]表示从 (i, j) 出发能达到的『最长递增路径』的长度
        memo = [[-1 for _ in matrix[0]] for _ in matrix]
        maxLen = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                curLen = traverse(i, j, memo)
                maxLen = max(maxLen, curLen)

        return maxLen
