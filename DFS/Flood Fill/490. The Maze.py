""" 「」
# 与常规迷宫的不同在于本题并不需要枚举出地图中每一个点, 只需要枚举出靠墙的点即可。
* 从起始位置开始, 每次选择一条路线进行搜索, 并用一个二维布尔数组 visited 表示是否曾经到达过位置 (i, j)
* 若在某一次搜索到位置 (i, j) 时, visited[i, j] = true, 那么我们可以进行回溯, 不必继续搜索下去。

? https://leetcode.cn/problems/the-maze/solution/zhong-gui-zhong-ju-dfsji-bfs-liang-chong-bian-li-f/


? DFS 幻灯片: https://leetcode.cn/problems/the-maze/solution/mi-gong-by-leetcode/ 
/ 时间复杂度: O(MN), 其中 M 和 N 是迷宫的高和宽。
/ 空间复杂度: O(MN)。
"""


class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        numRows = len(maze)
        numCols = len(maze[0])

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        dir_x = [0, 0, 1, -1]
        dir_y = [1, -1, 0, 0]

        visited = [[False for _ in range(numCols)] for _ in range(numRows)]

        def DFS(curRow, curCol):
            if curRow == destination[0] and curCol == destination[1]:
                return True

            #! 与其他岛屿类问题的「不同之处」在于 DFS 的时候, 因为每次会被检视的 position都必定是 inArea 的, 所以不需要关心超界的 case, 只需要关心当前单元格是否「已被访问」
            if visited[curRow][curCol]:
                return False

            visited[curRow][curCol] = True

            # * 对四个方向进行遍历
            for i in range(4):
                newRow = curRow
                newCol = curCol
                # * 这里模拟的是小球的滚动过程, 题目中说"在遇到墙壁前不会停止滚动", 所以只要球在范围内并且当前位置是空地(0), 就一直滚动下去, 直到不满足其中「任何一个条件」
                while inArea(newRow, newCol) and maze[newRow][newCol] == 0:
                    newRow += dir_x[i]
                    newCol += dir_y[i]

                # * 这里需要「回滚一次」, 回到"出界前或者遇到墙壁前的「最后一个」合法位置"
                newRow -= dir_x[i]
                newCol -= dir_y[i]

                # * 然后对这个位置向四周进行 DFS, 如果有任何一个方向能够到达 destination, 直接返回 True
                directionRes = DFS(newRow, newCol)
                if directionRes:
                    return True

            return False

        return DFS(start[0], start[1])
