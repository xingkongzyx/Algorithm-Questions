""" 
* 这道题与542 非常相似
? 542 题解: https://leetcode.cn/problems/01-matrix/solution/tao-lu-da-jie-mi-gao-dong-ti-mu-kao-cha-shi-yao-2/
? https://leetcode.cn/problems/walls-and-gates/solution/qiang-yu-men-by-leetcode/
"""


class Solution:
    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        from collections import deque
        numRows = len(rooms)
        numCols = len(rooms[0])

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        queue = deque([])
        visited = [[False for _ in range(numCols)] for _ in range(numRows)]

        for i in range(numRows):
            for j in range(numCols):
                # if it is a gate.
                if rooms[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = True

        steps = 0
        x_dir = [0, 0, 1, -1]
        y_dir = [1, -1, 0, 0]
        while queue:
            steps += 1
            qLen = len(queue)
            for _ in range(qLen):
                curX, curY = queue.popleft()
                for i in range(4):
                    newX, newY = curX + x_dir[i], curY + y_dir[i]
                    # * 如果邻居单元格在范围内, 并且还没有被访问过, 并且这个单元格是一个empty room, 则说明从门出发能够成功抵达这个 room, 所需要的步数是 steps
                    if inArea(newX, newY) and visited[newX][newY] == False and rooms[newX][newY] == 2147483647:
                        queue.append((newX, newY))
                        # * 将其标记为已访问过, 防止死循环
                        visited[newX][newY] = True
                        rooms[newX][newY] = steps
