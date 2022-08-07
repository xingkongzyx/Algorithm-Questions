""" 
# 最重要需要理解的地方: 为什么不像其他岛屿类题目一样使用 visited 数组, 也没有改变已经访问过的位置的元素?
* 因为在递归终止条件中, "pre >= matrix[rowIdx][colIdx]" 确保了之前已经访问过的元素根本就不会出现在后续的路径里, 所以 visited 就没有存在的意义,。或者说题目中要求是搜索元素递增的最长深度，所以元素递增可以作为元素是否被访问的标志，
"""


class Solution(object):
    def longestIncreasingPath(self, matrix):
        numRows = len(matrix)
        numCols = len(matrix[0])

        maxLen = 0

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        def traverse(rowIdx, colIdx, pre):
            if inArea(rowIdx, colIdx) == False or pre >= matrix[rowIdx][colIdx]:
                return 0

            curLen = 1
            leftLen = curLen + \
                traverse(rowIdx, colIdx - 1, matrix[rowIdx][colIdx])
            rightLen = curLen + \
                traverse(rowIdx, colIdx + 1, matrix[rowIdx][colIdx])
            topLen = curLen + \
                traverse(rowIdx - 1, colIdx, matrix[rowIdx][colIdx])
            botLen = curLen + \
                traverse(rowIdx + 1, colIdx, matrix[rowIdx][colIdx])

            return max(leftLen, rightLen, topLen, botLen)

        for i in range(numRows):
            for j in range(numCols):
                curLen = traverse(i, j, float("-inf"))
                maxLen = max(curLen, maxLen)

        return maxLen
