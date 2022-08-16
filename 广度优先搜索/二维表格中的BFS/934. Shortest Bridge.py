""" 「」
* ➀ 遍历矩阵, 找到第一个岛, 调用 dfs 把和第一个岛联通的所有 1 改成 2, 并且加入队列, 作为多源广度搜索的source
* ➁ 调用「多源」广度搜索把第一个岛向周围扩散(即把它把周围的0改为2), 直到在某次扩散时遇到 1, 说明已经遇到了另一个岛, 此时返回扩散的次数即可。
? https://leetcode.cn/problems/shortest-bridge/solution/zui-duan-qiao-yan-sou-shen-sou-by-liangqi/
"""
from collections import deque


class Solution(object):
    def shortestBridge(self, grid):
        numRows = len(grid)
        numCols = len(grid[0])
        dirArr = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        # * 把找到的「第一个岛」的格子全部染成 2, 同时把整个个岛的所有坐标放到队列 queue
        def DFS(rowIdx, colIdx, queue):
            if inArea(rowIdx, colIdx) == False \
                or grid[rowIdx][colIdx] == 2 or \
                    grid[rowIdx][colIdx] == 0:
                return

            grid[rowIdx][colIdx] = 2
            queue.append((rowIdx, colIdx))
            for i in range(4):
                newRowIdx = rowIdx + dirArr[i][0]
                newColIdx = colIdx + dirArr[i][1]
                DFS(newRowIdx, newColIdx, queue)

        # * 从找到的「第一个岛」开始「多源」广度搜索, 每扩展一层, res+1, 直到找到「第二个岛」
        def BFS(queue):
            res = 0
            while queue:
                numOfNodesInLevel = len(queue)
                for _ in range(numOfNodesInLevel):
                    currentX, currentY = queue.popleft()

                    for i in range(4):
                        newX, newY = currentX + \
                            dirArr[i][0], currentY + dirArr[i][1]

                        # * 只有当前坐标的邻居坐标「不越界」并且这个邻居「没有」被访问过(值不为 2)才继续下面步骤
                        if inArea(newX, newY) and grid[newX][newY] != 2:
                            # # 如果值为 1, 说明找到了「第二个岛」, 直接返回 res
                            if grid[newX][newY] == 1:
                                return res
                            grid[newX][newY] = 2
                            queue.append((newX, newY))
                res += 1

        queue = deque([])
        for i in range(numRows):
            for j in range(numCols):
                # * 使用 DFS 将第一座岛进行标识(通过将对应的值改为2来实现)
                if grid[i][j] == 1:
                    DFS(i, j, queue)
                    res = BFS(queue)
                    return res


Solution().shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]])
