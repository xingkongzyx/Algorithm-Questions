""" 
> 做本题之前, 建议先做 200题和695题, 然后再做本题, 本题是前两个的一个延伸。
* 这道题实际上是对网格做了两次遍历: 
* 1.第一次是DFS遍历, 先深度优先遍历出每一个「独立岛屿」, 计算每个「岛屿」的面积并标记「岛屿」(做法是将同一块「岛屿」中的格子值设置为为同一索引值 idx), 然后将「岛屿索引」以及对应的这块「岛屿的面积」存储在 hashmap 中, 方便后续调用. 一旦遍历到新的陆地就累加 idx, 这样 idx 将代表岛屿面积 map 中的索引值, 便于后续查找面积。
* 补充: 因为 0 代表海洋, 1 代表陆地, 我们不能选择 0 和 1, 那么我们就从 2 开始编号
* 2.第二次遍历, 一旦发现海洋, 就判断上下左右格子是否为「陆地」, 此处要特别注意的是, 有可能四周皆为陆地, 但需要判断这些陆地是「同一块」陆地, 还是「不同」的陆地, 避免陆地面积重复累加, 这里是个易错点。
「」

! 第二次遍历严格意义上来说并不算 DFS, 只是简单地提取邻居「岛屿」的面积, 然后对每个改变「海洋」格子后构成的新的「岛屿」的面积进行比较, 选出一个最大的则是答案
? https://leetcode.cn/problems/making-a-large-island/solution/dfs-shi-xian-zui-da-ren-gong-dao-wen-ti-hsmqq/
? https://leetcode.cn/problems/making-a-large-island/solution/jian-dan-yi-yu-li-jie-de-java-dfsfang-fa-by-caipen/
/ 时间复杂度: O(N^2), 其中 N 是 grid 的长度和宽度。
/ 空间复杂度: O(N^2), 深度优先搜索需要的数组 area 的额外空间。

"""


class Solution(object):
    def largestIsland(self, grid):
        record = {}
        # * idx 表示岛屿的编号, 0是海洋1是陆地, 从2开始遍历
        idx = 2
        totalRows = len(grid)
        totalCols = len(grid[0])
        maxArea = 0

        dir_x = [0, 0, 1, -1]
        dir_y = [1, -1, 0, 0]

        # * 计算每个岛屿的面积, 并标记是第几个岛屿
        def calculateArea(rowIdx, colIdx, idx):
            if inArea(rowIdx, colIdx) == False or grid[rowIdx][colIdx] != 1:
                return 0

            # * 直接对这个岛屿的值进行更改从而标记它是第几个岛屿
            grid[rowIdx][colIdx] = idx
            cur = 1
            for i in range(4):
                newRowIdx = rowIdx + dir_x[i]
                newColIdx = colIdx + dir_y[i]
                cur += calculateArea(newRowIdx, newColIdx, idx)

            return cur

        def changeSea(rowIdx, colIdx):
            helper = set()
            areaAfterChangeWater = 1

            # * 如果想要访问的「方向坐标」在 grid 范围内, 并且它是片陆地(grid的值大于2), 并且还没有被记录在 helper set中, 则在 record 中找到对应的面积, 并加在用于记录将这块海洋改成陆地的变量 areaAfterChangeWater 上
            for i in range(4):
                newRowIdx = rowIdx + dir_x[i]
                newColIdx = colIdx + dir_y[i]

                if inArea(newRowIdx, newColIdx) \
                        and grid[newRowIdx][newColIdx] > 1 \
                        and grid[newRowIdx][newColIdx] not in helper:
                    areaAfterChangeWater += record.get(
                        grid[newRowIdx][newColIdx])
                    helper.add(grid[newRowIdx][newColIdx])

            return areaAfterChangeWater

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < totalRows and 0 <= colIdx < totalCols

        for i in range(totalRows):
            for j in range(totalCols):
                if grid[i][j] == 1:
                    curArea = calculateArea(i, j, idx)
                    record[idx] = curArea
                    idx += 1

        #* 遍历海洋, 找到相邻陆地面积最大的海洋格子
        for i in range(totalRows):
            for j in range(totalCols):
                if grid[i][j] == 0:
                    curArea = changeSea(i, j)
                    maxArea = max(maxArea, curArea)

        # * 可能都没有海洋, 全是陆地, 则再次判断, 直接返回陆地最大值
        if maxArea == 0:
            maxArea = record.get(2)
        # print(maxArea)
        return maxArea


# Solution().largestIsland([[1, 1], [1, 1]])
