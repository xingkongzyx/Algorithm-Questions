""" 「」
* 题目要求：返回直到单元格中没有新鲜橘子为止所必须经过的「最小分钟数」。翻译一下, 实际上就是求腐烂橘子到所有新鲜橘子的「最短路径」

* 由于可能存在「无法被污染」的橘子, 我们需要记录新鲜橘子的数量, 也就是代码中的变量 count。在 BFS 中, 每遍历到一个橘子（污染了一个橘子）, 就将新鲜橘子的数量减一。如果 BFS 结束后这个数量仍未减为零, 说明存在「无法被污染」的橘子。


* 多源BFS 与 普通BFS 并无特别明显的区别, 普通的BFS就是要以一个起点开始进行扩散, 而多源BFS就是以多个起点一起开始进行扩散, 方法就是在队列中先记录当前队列的长度, 将这个长度作为每一轮扩散的数量依据。

? https://leetcode.cn/problems/rotting-oranges/solution/li-qing-si-lu-wei-shi-yao-yong-bfsyi-ji-ru-he-xie-/

/ 思路详细叙述
/ 1.刚开始将所有烂橘子位置压入队列, 并统计新鲜橘子数量;
/ 2.bfs从烂橘子位置开始遍历, 让所有新鲜橘子摆烂, 并且把本次摆烂的橘子压入队列;
/ 3.由上一层摆烂的橘子继续向其四周扩散, 以此层层迭代;
/ 4.随着摆烂蔓延, 新鲜橘子越来越少, 最后判断时间;
? https://leetcode.cn/problems/rotting-oranges/solution/ji-jian-si-lu-bfs-javaban-ben-by-ren-fei-ugc1/
"""


class Solution:
    def orangesRotting(self, grid):
        numRows = len(grid)
        numCols = len(grid[0])
        dir_arr = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        queue = []
        # * count 表示新鲜橘子的数量
        count = 0
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 1:
                    count += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        # * round 表示腐烂的轮数, 或者分钟数
        round = 0
        #! 如果没有「count > 0」这一限定条件, 因为队列中最后一层橘子遍历后时间会加 1,但没有橘子被继续感染,此处会多了一次 1
        # * 还有新鲜的橘子且队列还有腐烂的橘子
        while count > 0 and len(queue) > 0:
            # * 分钟数 +1
            round += 1
            # * 记录这一层的腐烂的橘子数
            numOfLevelNodes = len(queue)
            # * 遍历完这一层的腐烂的橘子
            for _ in range(numOfLevelNodes):
                # * 取出队列开头的腐烂的橘子坐标
                r, c = queue.pop(0)
                for dir_x, dir_y in dir_arr:
                    newRowIdx = r + dir_x
                    newColIdx = c + dir_y
                    # * 如果四个方向有「新鲜」的橘子。注意, 必须得是「新鲜」的橘子才能被感染, 如果 grid[i][j] == 0, 代表 an empty cell, 是不能被感染的
                    if inArea(newRowIdx, newColIdx) and grid[newRowIdx][newColIdx] == 1:
                        # * 新鲜橘子变腐烂, 避免它被「重复遍历」
                        grid[newRowIdx][newColIdx] = 2
                        # * 新鲜的橘子数-1
                        count -= 1
                        # * 新变坏的这只橘子进入坏橘子队列
                        queue.append((newRowIdx, newColIdx))
        # * 如果还有新鲜的橘子
        if count > 0:
            return -1
        else:
            # * 没有新鲜的橘子了
            return round
