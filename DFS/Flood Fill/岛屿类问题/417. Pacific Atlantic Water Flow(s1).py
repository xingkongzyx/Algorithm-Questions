"""
* 对于一个点它能流动到两边的大洋, 那么反过来, 两边大洋的水反着流就能达到这个点。既然水开始倒流了, 那么逻辑也需要反过来, 因此只有当下一个点的高度比当前的点的高度「大于或等于」时, 水才能流过去。
* 为什么这么考虑呢？试想一下, 如果采用「正序」, 我们需要对「每个来源」(本题里即每个节点)做 DFS, 看它是否符合要求。如果采用「倒序」的话, 我们只要从结果开始往上溯源。在本题里, 结果是四条边。明显, 结果数量远小于来源。
? https://leetcode.cn/problems/pacific-atlantic-water-flow/solution/tai-ping-yang-da-xi-yang-shui-liu-wen-ti-f86l/

* 主要步骤: 将水的流向反转, 假设太平洋和大西洋的水「从低向高」攀登, 分别能到达哪些位置, 分别用 p_visited 和 a_visited 表示。两者的『交集』就代表能「同时」流向太平洋和大西洋的位置。

? 思路来源: https://leetcode.cn/problems/pacific-atlantic-water-flow/solution/by-fuxuemingzhu-jqz4/
? 代码来源: https://leetcode.cn/problems/pacific-atlantic-water-flow/solution/417java-dfscong-bian-yuan-wang-li-fang-wen-xiang-j/


/ 时间复杂度: O(mn), 其中 m 和 n 分别是矩阵 heights 的行数和列数。深度优先搜索最多遍历每个单元格两次, 寻找太平洋和大西洋都可以到达的单元格需要遍历整个矩阵, 因此时间复杂度是 O(mn)。
/ 空间复杂度: O(mn), 其中 m 和 n 分别是矩阵 heights 的行数和列数。深度优先搜索的递归调用层数是 O(mn), 记录每个单元格是否可以到达太平洋和大西洋需要 O(mn) 的空间, 因此空间复杂度是 O(mn)。
"""


class Solution(object):
    def pacificAtlantic(self, heights):
        x_dir = [0, 0, 1, -1]
        y_dir = [1, -1, 0, 0]

        numRows = len(heights)
        numCols = len(heights[0])

        def traverse(rowIdx, colIdx, visited):
            # * when dfs called, meaning its caller already verified this point
            visited[rowIdx][colIdx] = True

            # * 检查四个方向的相邻节点, 如果某一个方向的相邻节点坐标满足下面的全部三个条件, 则对其进行 DFS 遍历
            # *  ➀ 不越界
            # *  ➁ 对应的值「大于等于」当前坐标的值
            # *  ➂ 没有被访问过
            for i in range(4):
                newRowIdx = rowIdx + x_dir[i]
                newColIdx = colIdx + y_dir[i]

                if inArea(newRowIdx, newColIdx) and \
                   visited[newRowIdx][newColIdx] == False and \
                   heights[newRowIdx][newColIdx] >= heights[rowIdx][colIdx]:
                    # > doing DFS from the present cell to the neighbors from which it can receive the water.
                    traverse(newRowIdx, newColIdx, visited)

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        pacificVisited = [
            [False for _ in range(numCols)] for _ in range(numRows)]
        atlanticVisited = [
            [False for _ in range(numCols)] for _ in range(numRows)]

        # * 左右两边加上下两边出发深搜
        for colIdx in range(numCols):
            # * 找到从太平洋边界倒流能到达的所有位置
            traverse(0, colIdx, pacificVisited)
            # * 找到从大西洋边界倒流能到达的所有位置
            traverse(numRows - 1, colIdx, atlanticVisited)

        for rowIdx in range(numRows):
            # * 找到从太平洋边界倒流能到达的所有位置
            traverse(rowIdx, 0, pacificVisited)
            # * 找到从大西洋边界倒流能到达的所有位置
            traverse(rowIdx, numCols - 1, atlanticVisited)

        resultList = []
        # * 找到两者的交集即为答案
        for i in range(numRows):
            for j in range(numCols):
                if pacificVisited[i][j] == True and atlanticVisited[i][j] == True:
                    resultList.append([i, j])

        return resultList


Solution().pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
    2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
