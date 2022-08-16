""" 
! 当前暴力解法超出时间限制
/ 时间复杂度: O(N^2 * M^2)
"""


class Solution:
    def updateMatrix(self, mat):
        x_dir = [0, 0, -1, 1]
        y_dir = [1, -1, 0, 0]
        numRows = len(mat)
        numCols = len(mat[0])

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        res = [[0 for _ in range(numCols)] for _ in range(numRows)]

        def BFS(rowIdx, colIdx):
            # * steps 代表从当前的「元素 1」- mat[rowIdx][colIdx], 出发到「最近的 0」的距离。
            steps = 0
            queue = [(rowIdx, colIdx)]
            # * 使用「暴力解法」, 每次从「元素 1」出发时都要重新进行一遍 BFS, 所以每次都需要一个 visited 数组
            visited = [[False for _ in range(numCols)] for _ in range(numRows)]
            visited[rowIdx][colIdx] = True

            while queue:
                numOfNodesInLevel = len(queue)

                for _ in range(numOfNodesInLevel):
                    poppedNode = queue.pop(0)
                    currentX, currentY = poppedNode[0], poppedNode[1]
                    # * 只要遇到了0, 说明找到了从「元素 1」的「最近的 0」, 直接返回他们之间的距离 steps
                    if mat[currentX][currentY] == 0:
                        return steps

                    for dirIdx in range(4):
                        newX, newY = currentX + \
                            x_dir[dirIdx], currentY + y_dir[dirIdx]
                        # * 在本轮就把下一轮要访问的元素检查是否访问过, 没有的话加入队列并标记为「已访问」
                        if inArea(newX, newY) and visited[newX][newY] == False:
                            visited[newX][newY] = True
                            queue.append((newX, newY))

                steps += 1

        for i in range(numRows):
            for j in range(numCols):
                if mat[i][j] == 1:
                    res[i][j] = BFS(i, j)

        return res


print(Solution().updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
