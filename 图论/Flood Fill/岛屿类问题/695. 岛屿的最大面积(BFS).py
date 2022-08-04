""" 
/ 时间复杂度：O(m * n)
/ 空间复杂度：O(m * n)，主要在queue这里，最坏情况全部是土地，大概能到O(m * n)这个级别

? https://leetcode.cn/problems/max-area-of-island/solution/695-dao-yu-de-zui-da-mian-ji-dfs-bfsshua-oe8m/


"""


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        def BFS(x, y):
            from collections import deque
            queue = deque()
            queue.append((x, y))
            currentArea = 0
            while len(queue) > 0:
                currentX, currentY = queue.popleft()
                if currentX < 0 or currentX >= rows or currentY < 0 or currentY >= cols or grid[currentX][currentY] == 0:
                    continue

                currentArea += 1
                grid[currentX][currentY] = 0
                queue.append((currentX + 1, currentY))
                queue.append((currentX - 1, currentY))
                queue.append((currentX, currentY + 1))
                queue.append((currentX, currentY - 1))
            return currentArea

        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    currentArea = BFS(i, j)
                    maxArea = max(currentArea, maxArea)
        return maxArea
