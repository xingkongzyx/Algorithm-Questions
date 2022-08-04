""" 
* 相同形状的岛的判断标准：将一块岛屿的「起始坐标」作为「相对原点」, 相同形状的岛只需要所有的点的「相对坐标」都一样就可以了, 也就是『当前位置的相对坐标 = 当前位置的真实坐标 - 这块岛屿相对原点的坐标』
# 采用深度优先搜索, 将搜索到的构成每一座「岛屿」的所有陆地位置的「相对坐标」保存成字符串, 这个字符串用 set 保存并去重, 这样形状相同的岛屿就不会被记录在 set 中, 最后返回 set 的大小就好
? https://leetcode.cn/problems/number-of-distinct-islands/solution/javashen-du-you-xian-sou-suo-hashsetqu-zhong-by-we/ 
"""


class Solution(object):
    def numDistinctIslands(self, grid):
        numRows = len(grid)
        numCols = len(grid[0])
        result = set()

        def traverse(rowIdx, colIdx, startRow, startCol):
            if inArea(rowIdx, colIdx) == False or grid[rowIdx][colIdx] != 1:
                return

            grid[rowIdx][colIdx] = 2
            # * 在 currentPath 中存储的是当前位置的「相对坐标」
            currentPath.append(rowIdx - startRow)
            currentPath.append(colIdx - startCol)
            traverse(rowIdx + 1, colIdx, startRow, startCol)
            traverse(rowIdx - 1, colIdx, startRow, startCol)
            traverse(rowIdx, colIdx + 1, startRow, startCol)
            traverse(rowIdx, colIdx - 1, startRow, startCol)

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == 1:
                    currentPath = []
                    traverse(i, j, i, j)
                    # * 每遍历完成一座「岛屿」，将构成这座「岛屿」的所有陆地位置的「相对坐标」保存成字符串，然后加入 result set 保存并同时起到去除形状相同的岛屿的作用
                    pathStr = ''.join([str(ele) for ele in currentPath])

                    result.add(pathStr)
        # * 最后, result set 的长度即为所求
        return len(result)


Solution().numDistinctIslands(
    [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]])
