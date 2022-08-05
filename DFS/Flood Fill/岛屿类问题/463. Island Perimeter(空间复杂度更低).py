""" 
https://leetcode.cn/problems/island-perimeter/solution/shou-hua-tu-jie-463-dao-yu-de-zhou-chang-by-xiao_b/

#* 一块土地原则上会带来 4 个周长，但岛上的土地存在接壤，每一条接壤，会减掉 2 个边长。

#* 所以，总周长 = 4 * 土地个数 - 2 * 接壤边的条数。

#* 遍历矩阵，遍历到土地，就 land++，如果它的右/下边也是土地，则 border++，遍历结束后代入公式。
O(n * m) | time
O(1) | space
"""


class Solution(object):
    def islandPerimeter(self, grid):
        lands = 0
        boarders = 0
        for rowIdx in range(0, len(grid)):
            for colIdx in range(0, len(grid[0])):
                if grid[rowIdx][colIdx] == 1:
                    lands += 1
                    if(colIdx < len(grid[0]) - 1 and grid[rowIdx][colIdx + 1] == 1):
                        boarders += 1
                    if(rowIdx < len(grid) - 1 and grid[rowIdx + 1][colIdx] == 1):
                        boarders += 1
        # print(f"lands are {lands}, boarders are {boarders}")
        return 4 * lands - 2 * boarders


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
s = Solution()
res = s.islandPerimeter(grid)
print(res)
