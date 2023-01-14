""" 「」
> 本题与1162. 地图分析是一样的思路。
* 矩阵中的 0 有很多个, 要求「最近」的 0, 最直观的思路就是: 每次从一个 1 出发一圈圈扩展(BFS), 遇到的「第一个 0」就是所谓「最近的」。这就是暴力思路, 然而矩阵中的每个元素(位置)是一个结点(状态), 对于这MN个结点, 每个进行一次 O(MN) 的BFS, 时间复杂度就到了O(N^2 * M^2), 肯定会超时。
? 暴力解法的代码: https://leetcode.cn/problems/01-matrix/solution/bao-li-duo-yuan-bfsdpdpyou-hua-dai-zheng-ming-by-b/
? 暴力思路的问题: https://leetcode.cn/problems/01-matrix/solution/ni-xiang-si-wei-de-bfscshi-xian-by-da-fei-kai/

* 优化思路基于「逆向思维」: 不再从1出发, 而是从所有的0出发(而且是同时出发)进行BFS, 就像评论中说的「填海造陆」。0 扩展到的每一层 1, 对于这些 1 来说, 都找到了最近的 0, 距离就是BFS的层数。

? 优化代码: https://leetcode.cn/problems/01-matrix/solution/tao-lu-da-jie-mi-gao-dong-ti-mu-kao-cha-shi-yao-2/
"""


class Solution:
    def updateMatrix(self, mat):
        x_dir = [0, 0, -1, 1]
        y_dir = [1, -1, 0, 0]
        numRows = len(mat)
        numCols = len(mat[0])
        visited = [[False for _ in range(numCols)] for _ in range(numRows)]
        res = [[0 for _ in range(numCols)] for _ in range(numRows)]

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        queue = []
        # > 在向队列中加入下一轮要处理的节点的时候, 将其对应的 visited数组 以及 结果数组 进行更新
        for i in range(numRows):
            for j in range(numCols):
                # * 首先把所有为 0 的元素的坐标加入队列, 并将 visited 的对应位置标记为「已访问」
                # # 在本轮就把下一轮要访问的元素标记为「已访问」
                if mat[i][j] == 0:
                    visited[i][j] = True
                    queue.append((i, j))

        steps = 0
        while queue:
            steps += 1
            numOfNodesInLevel = len(queue)
            # * 对 queue 中当前层的所有元素进行遍历, 对弹出的每个元素的「上下左右」四个邻居进行判断, 判断「邻居」是否越界以及是否「已访问」
            for i in range(numOfNodesInLevel):

                currentX, currentY = queue.pop(0)

                for dirIdx in range(4):
                    newX, newY = currentX + \
                        x_dir[dirIdx], currentY + y_dir[dirIdx]
                    # # 在本轮就把下一轮要访问的元素标记为「已访问」, 并且对应的结果数组进行更新
                    if inArea(newX, newY) and visited[newX][newY] == False:
                        res[newX][newY] = steps
                        visited[newX][newY] = True
                        queue.append((newX, newY))
        return res


Solution().updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]])
# Solution().updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [0, 0, 0]])
