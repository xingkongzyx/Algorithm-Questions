""" 
主循环和DFS类似，不同点是在于搜索某岛屿边界的方法不同。
bfs 方法：
    1. 借用一个队列 queue，判断队列首部节点 (i, j) 是否未越界且为 1：
        1.1 若是则置零（删除岛屿节点），并将此节点上下左右节点 (i+1,j),(i-1,j),(i,j+1),(i,j-1) 加入队列；
        1.2 若不是则跳过此节点；
    2. 循环 popleft 队列首节点，直到整个队列为空，此时已经遍历完此岛屿。

作者：jyd
链接：https://leetcode.cn/problems/number-of-islands/solution/number-of-islands-shen-du-you-xian-bian-li-dfs-or-/
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def BFS(xIdx, yIdx):
            from collections import deque
            queue = deque()
            queue.append((xIdx, yIdx))
            while len(queue):
                currentX, currentY = queue.popleft()
                if currentX >= rows or currentY >= cols or currentX < 0 \
                    or currentY < 0 or grid[currentX][currentY] == "0":
                    continue

                grid[currentX][currentY] = "0"

                queue.append((currentX + 1, currentY))                
                queue.append((currentX - 1, currentY))                
                queue.append((currentX, currentY + 1))                
                queue.append((currentX, currentY - 1))                
        


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    BFS(i, j)
        return count


