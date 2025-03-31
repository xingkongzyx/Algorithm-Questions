""" 
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
        # > 在向队列中加入下一轮要处理的节点的时候, 对其对应的 visited数组 进行更新
        # ! visited 必须在扩展时就立即标记visited状态，而不是等到出队列才标记。否在会导致同一个水域节点可能被多次加入队列，从而造成距离（level）的错误计算。
        """ 
! 用 542 进行理解更加形象
好的，我来给您一个明确的例子，展示当在出队时标记访问会导致错误结果的情况。

在出队时标记导致错误结果的例子
考虑以下3×3网格：

0 0 0
0 1 0
0 0 0
这里只有中心位置(1,1)是陆地，其他都是水域。问题是求最远的水域到陆地的距离。

正确答案
正确的结果是2，因为四个角落(0,0)、(0,2)、(2,0)和(2,2)都需要通过两步才能到达中心的陆地。

使用错误的标记时机（出队时标记）
初始状态：

队列中有陆地位置：[(1,1)]
所有位置都未访问
level = -1
第一轮BFS（level变为0）：

出队(1,1)，标记(1,1)为已访问
检查(1,1)的邻居：(0,1)、(1,0)、(1,2)、(2,1)都是未访问的水域，加入队列
此时队列：[(0,1), (1,0), (1,2), (2,1)]

第二轮BFS（level变为1）：

出队(0,1)，标记(0,1)为已访问
检查(0,1)的邻居：(0,0)和(0,2)是未访问的水域，加入队列
出队(1,0)，标记(1,0)为已访问
检查(1,0)的邻居：(0,0)和(2,0)是未访问的水域，加入队列
注意，(0,0)被加入队列第二次！因为虽然之前已加入，但还未标记为已访问
出队(1,2)，标记(1,2)为已访问
检查(1,2)的邻居：(0,2)和(2,2)是未访问的水域，加入队列
注意，(0,2)被加入队列第二次！
出队(2,1)，标记(2,1)为已访问
检查(2,1)的邻居：(2,0)和(2,2)是未访问的水域，加入队列
注意，(2,0)和(2,2)都被加入队列第二次！
此时队列：[(0,0), (0,2), (0,0), (2,0), (0,2), (2,2), (2,0), (2,2)]
角落位置每个都重复出现了！

第三轮BFS（level变为2）：

处理队列中的位置，包括重复的角落位置
但是问题来了：
在第三轮中，队列里有很多重复位置。当处理第一个(0,0)时，它会被标记为已访问，但队列中仍有另一个(0,0)在等待处理。

当处理重复的(0,0)时，所有邻居都已访问，所以不会加入新位置。但level仍会增加到3，因为队列不为空。

最终返回level=3，而正确答案应该是2！

使用正确的标记时机（入队时标记）
初始状态：

队列中有陆地位置：[(1,1)]，并已标记为已访问
level = 0
第一轮BFS：

出队(1,1)
检查(1,1)的邻居：加入(0,1)、(1,0)、(1,2)、(2,1)并立即标记为已访问
此时队列：[(0,1), (1,0), (1,2), (2,1)]

第二轮BFS（level变为1）：

出队(0,1)
检查邻居(0,0)和(0,2)，加入并标记为已访问
出队(1,0)
检查邻居(0,0)已访问，只加入(2,0)并标记
出队(1,2)
检查邻居(0,2)已访问，只加入(2,2)并标记
出队(2,1)
检查邻居(2,0)和(2,2)已访问，不加入新位置
此时队列：[(0,0), (0,2), (2,0), (2,2)]

第三轮BFS（level变为2）：

处理角落位置，它们都没有未访问的邻居了
队列变为空，BFS结束
返回level=2，这是正确答案！

错误关键点
出队时标记的问题在于：

同一个位置可能从不同路径被多次发现并加入队列
这会导致BFS的层级计算不准确，因为本应在第n层处理完的位置可能出现在第n+1层
最终结果会高估最远距离
这个例子清晰地展示了为什么在BFS中正确的做法是在入队时就标记节点为已访问，而不是在出队时标记。
        
         """
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
