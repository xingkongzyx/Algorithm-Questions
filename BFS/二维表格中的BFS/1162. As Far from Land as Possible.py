""" 
> 本题与1162. 地图分析是一样的思路。
* 对于本题, 如果套用「单源最短路」做法, 我们需要对每个「海洋」位置做一次 BFS：求得每个「海洋」的最近陆地距离, 然后在所有的距离中取 max 作为答案。时间复杂度为 O(n⁴), 不符合要求
? 为什么不能从海洋开始遍历: https://leetcode.cn/problems/as-far-from-land-as-possible/solution/gong-shui-san-xie-ru-he-shi-yong-duo-yua-vlea/
! 这道题实际上就是求「海洋」格子到「陆地」格子的「最长路径」. 也就是从「陆地 1」开始, 要扩散多少次, 才能把所有的「海洋」给覆盖掉. 「最远」应该从这个角度来理解. BFS 能求最短路径, 自然也能求最长路径. 那么这道题使用 BFS, 应该是毫无疑问的了. 
? https://leetcode.cn/problems/as-far-from-land-as-possible/solution/tao-lu-da-jie-mi-gao-dong-ti-mu-kao-cha-shi-yao-sh/
? https://leetcode.cn/problems/as-far-from-land-as-possible/solution/li-qing-si-lu-wei-shi-yao-yong-bfs-ru-he-xie-bfs-d/

/ 时间复杂度: O(N^2), 这里 NN 是方格的边长。二维表格里所有的元素都会被看一遍；
/ 空间复杂度: O(N^2), 最坏情况下, 方格里全部是陆地的时候, 元素全部会进队列。

"""


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        visited = [[False for _ in range(numCols)] for _ in range(numRows)]
        queue = []
        numLands = 0
        # * 将所有陆地都放入队列中
        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == 1:
                    numLands += 1
                    visited[i][j] = True
                    queue.append((i, j))
        # * 如果没有陆地或者海洋, 返回-1
        if numLands == 0 or numLands == numRows * numCols:
            return -1

        dirArr = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # * 由于BFS的第一层遍历是从陆地开始, 因此遍历完第一层之后distance应该是0
        res = -1
        while queue:
            numOfNodesInLevel = len(queue)

            for _ in range(numOfNodesInLevel):
                currentX, currentY = queue.pop(0)
                # * 对当前元素的各个方向进行搜索
                for i in range(4):
                    newX, newY = currentX + \
                        dirArr[i][0], currentY + dirArr[i][1]
                    # * 只有在搜索到的新坐标不超出范围并且没有被访问过的情况下, 才加入到队列中
                    if inArea(newX, newY) and visited[newX][newY] == False:
                        visited[newX][newY] = True
                        queue.append((newX, newY))
            res += 1
        # * 最终走了多少层才把海洋遍历完
        return res
