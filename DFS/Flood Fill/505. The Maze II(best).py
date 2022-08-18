""" 
> 只能用 BFS, python的DFS解法 一定会超时
* 使用一个二维数组 distance 记录从「起始位置」到 (i, j) 的最小步数 distance[i][j], 若在某一次搜索到位置 (i, j) 时, distance[i][j] 的值小于等于 count, 那么我们可以进行回溯, 不必继续搜索下去。
# 这道题中通过「数组distance」就可以判断出当前位置是否「已经访问过」, 就不用 visited 数组。

? 演示: https://leetcode.cn/problems/the-maze-ii/solution/mi-gong-ii-by-leetcode/
? 代码: https://leetcode.cn/problems/the-maze-ii/solution/c-python3-fa-1dfschao-shi-fa-2bfsbu-she-87l40/

* 特殊的BFS, 
* ① 不是每走一步都要加到队列中, 而是要撞到墙了才要加入队列中；
* ② 需要设置一个distance数组, 和maze大小相同, 全部初始化为无穷大
* ③ 每次出队, 需要在某个方向上走到底, 除非遇到边界或1, 则沿原来的相反方向回退一格, 即作为停止点；
* ④ 停止点要想加入队列, 需要判断当前前进方向的距离+到上一个起始点（也可能是停止点的距离）是否小于停止点上次记录的大小, 如果小于则更新, 加入队列, 否则不加队列, 继续行进。
? 解释参考: https://leetcode.cn/problems/the-maze-ii/solution/shi-yong-bfsbu-neng-yong-visitedju-chi-geng-xiao-j/

"""


class Solution:
    def shortestDistance(self, maze, start, destination) -> int:
        numRows, numCols = len(maze), len(maze[0])

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        distance = [[float('inf') for _ in range(numCols)]
                    for _ in range(numRows)]
        distance[start[0]][start[1]] = 0  # 注意初始化

        queue = [(start[0], start[1])]  # 从起点开始BFS
        dir_arr = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while queue:
            curRow, curCol = queue.pop(0)
            for dr, dc in dir_arr:
                newRow = curRow
                newCol = curCol
                directionLen = 0

                while inArea(newRow, newCol) and maze[newRow][newCol] == 0:
                    newRow += dr  # 一直沿着方向走下去
                    newCol += dc
                    directionLen += 1

                newRow -= dr  # 碰壁了, 回退一步
                newCol -= dc
                directionLen -= 1
                # * 在计算过程中, 如果计算出的距离比distance中保存的要小, 更新distance中的距离, 并将该点重新加入队列
                if distance[curRow][curCol] + directionLen < distance[newRow][newCol]:
                    distance[newRow][newCol] = distance[curRow][curCol] + \
                        directionLen
                    queue.append((newRow, newCol))

        if distance[destination[0]][destination[1]] == float('inf'):
            return -1
        else:
            return distance[destination[0]][destination[1]]
