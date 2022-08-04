""" 
* 每找到一块陆地, 都对其向四个方向进行 DFS 遍历。并且使用一个变量 count 记录遍历到的陆地的数量。DFS 遍历函数的作用是判断当前所在的陆地是否属于题目定义的飞地, 属于飞地的定义是 "从当前所在位置无法在任意次数的移动中离开网格边界". 如果四个方向都满足这个判别条件, 说明这片陆地中的所有格子都是飞地, 就把 count 加到总的 result 中。如果有任何一个方向的陆地连接到了边界, 则不对 result 进行任何操作, 因为这次 DFS 遍历过程中经过的所有陆地都不属于飞地

! 这里需要注意的细节是上下左右「四个方向」〖都要遍历〗到, 不能因为某个方向返回False 了就直接退出, 特别注意的是不能用 and 连接 4 个 DFS 递归调用, 否则可能被短路掉就不对了。
"""


class Solution(object):
    def numEnclaves(self, grid):
        numRows = len(grid)
        numCols = len(grid[0])
        result = 0

        def traverse(rowIdx, colIdx):
            # * 如果接触到了边界, 说明这片土地都不属于题目要求的「飞地」,返回 False
            if inArea(rowIdx, colIdx) == False:
                return False

            # * 如果接触到海洋或者是已经遍历过的陆地, 说明这个方向满足要求, 这片土地可能属于「飞地」, 返回 True
            if grid[rowIdx][colIdx] != 1:
                return True

            grid[rowIdx][colIdx] = 2
            # * count 用于记录 DFS 遍历过程中遍历到的「陆地」的数量
            nonlocal count
            count += 1
            left_check = traverse(rowIdx, colIdx - 1)
            right_check = traverse(rowIdx, colIdx + 1)
            top_check = traverse(rowIdx - 1, colIdx)
            bot_check = traverse(rowIdx + 1, colIdx)

            return left_check and right_check and top_check and bot_check

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == 1:
                    count = 0
                    # * 如果这块土地以及其进行延申的遍历结果都满足要求, 说明这片土地属于「飞地」, 更新result
                    enclaveCheck = traverse(i, j)
                    if enclaveCheck:
                        result += count

        return result
