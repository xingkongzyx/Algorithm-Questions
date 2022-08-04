"""
对于一个点它能流动到两边的大洋，那么反过来，两边大洋的水反着流就能达到这个点。
既然水开始倒流了，那么逻辑也需要反过来，因此只有将下一个点比当前的点大时或者等于当前点的高度时，水才能流过去。


? 代码: https://leetcode.cn/problems/pacific-atlantic-water-flow/solution/417java-dfscong-bian-yuan-wang-li-fang-wen-xiang-j/
https://leetcode.cn/problems/pacific-atlantic-water-flow/solution/by-fuxuemingzhu-jqz4/
? 图形非常号: https://leetcode.cn/problems/pacific-atlantic-water-flow/solution/shui-wang-gao-chu-liu-by-xiaohu9527-xxsx/
? 模板解法: https://leetcode.cn/problems/pacific-atlantic-water-flow/solution/ni-liu-dfs-yu-bfs-by-fibonacciwh/

"""


class Solution(object):
    def pacificAtlantic(self, heights):
        x_dir = [0, 0, 1, -1]
        y_dir = [1, -1, 0, 0]

        numRows = len(heights)
        numCols = len(heights[0])

        def traverse(rowIdx, colIdx, visited):
            # * 只有符合规则的点才能进入到递归中
            visited[rowIdx][colIdx] = True

            # * 检查四个方向，如果某一个方向的坐标满足 ➀不越界, ➁对应的值大于等于当前坐标的值, ➂没有被访问过, 则对那个方向进行 DFS 遍历
            for i in range(4):
                newRowIdx = rowIdx + x_dir[i]
                newColIdx = colIdx + y_dir[i]

                if inArea(newRowIdx, newColIdx) and \
                   visited[newRowIdx][newColIdx] == False and \
                   heights[newRowIdx][newColIdx] >= heights[rowIdx][colIdx]:
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
