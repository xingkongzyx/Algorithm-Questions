"""
* 与 lc.695 岛屿的最大面积 lc.200 岛屿数量 属于同类题目
# 这道题目不是「回溯」, 没有「撤销选择」这一步骤, 这道题不是说要找到一条路径, 所以说当寻找第二条路时原来第一条找过的点可以撤销, 重新使用；这道题是要让我们找到所有可达解, 所以只要走过的点, 就永远不能再走了。

# ? https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/
? 类似题目: https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/by-da-fei-de-tian-kong-dhms/

/ 时间复杂度: O(MN), 最差情况下, 机器人遍历矩阵所有单元格, 此时时间复杂度为 O(MN) 。
/ 空间复杂度: O(MN), 最差情况下, Set visited 内存储矩阵所有单元格的索引, 使用 O(MN) 的额外空间。
"""


class Solution(object):
    def movingCount(self, m, n, k):

        count = 0
        # * 用于标记当前格子是否被访问过
        visited = [[False for _ in range(n)] for _ in range(m)]

        def calculateIdx(rowIdx, colIdx):
            idxSum = 0
            while rowIdx > 0:
                idxSum += rowIdx % 10
                rowIdx //= 10

            while colIdx > 0:
                idxSum += colIdx % 10
                colIdx //= 10
            return idxSum

        def traverse(rowIdx, colIdx):
            # * 开始递归遍历, 需满足以下条件：
            # * 1）访问该位置未越界；
            # * 2）满足：位数和 < k；
            # * 3）该位置没有被访问过（标志数组的该位置未修改过, 为False）,
            # * 如果不满足以上任一情况, 都直接返回。

            # * 递归终止条件
            if inArea(rowIdx, colIdx) == False or visited[rowIdx][colIdx] == True or calculateIdx(rowIdx, colIdx) > k:
                return

            # * 当到达一个满足条件的格子, 用于记录运动范围的变量 count 加 1
            nonlocal count
            count += 1
            visited[rowIdx][colIdx] = True
            traverse(rowIdx + 1, colIdx)
            traverse(rowIdx - 1, colIdx)
            traverse(rowIdx, colIdx + 1)
            traverse(rowIdx, colIdx - 1)

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < m and 0 <= colIdx < n
        traverse(0, 0)

        return count
