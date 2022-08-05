"""
* 具体思路看 s1 解法
? 代码: https://leetcode.cn/problems/pacific-atlantic-water-flow/solution/ni-liu-dfs-yu-bfs-by-fibonacciwh/
"""


class Solution(object):
    def pacificAtlantic(self, heights):
        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        # * 使用了 preHeight 变量记录上一个位置的高度, 如果不符合当前高度大于等于上一个位置的高度的要求, 不能标记这个位置为 True
        def traverse(rowIdx, colIdx, preHeight, visited):
            # * 递归的终止条件, 也是对当前位置进行筛选的地方
            if inArea(rowIdx, colIdx) == False or \
                    visited[rowIdx][colIdx] == True or \
                    heights[rowIdx][colIdx] < preHeight:
                return

            visited[rowIdx][colIdx] = True
            # > doing DFS from the present cell to neighbours where the water can flow(与 s1 解法的不同之处, 这里没有任何的筛选, 四个方向都进行 dfs 遍历).
            traverse(rowIdx + 1, colIdx, heights[rowIdx][colIdx], visited)
            traverse(rowIdx - 1, colIdx, heights[rowIdx][colIdx], visited)
            traverse(rowIdx, colIdx + 1, heights[rowIdx][colIdx], visited)
            traverse(rowIdx, colIdx - 1, heights[rowIdx][colIdx], visited)

        numRows = len(heights)
        numCols = len(heights[0])
        pacificVisited = [
            [False for _ in range(numCols)] for _ in range(numRows)]
        atlanticVisited = [
            [False for _ in range(numCols)] for _ in range(numRows)]

        for i in range(numRows):
            traverse(i, 0, heights[i][0], pacificVisited)
            traverse(i, numCols - 1, heights[i][numCols - 1], atlanticVisited)

        for j in range(numCols):
            traverse(0, j, heights[0][j], pacificVisited)
            traverse(numRows - 1, j, heights[numRows - 1][j], atlanticVisited)

        resultList = []

        for i in range(numRows):
            for j in range(numCols):
                if pacificVisited[i][j] == True and atlanticVisited[i][j] == True:
                    resultList.append([i, j])

        return resultList
