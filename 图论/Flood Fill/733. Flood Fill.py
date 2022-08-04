""" 
! 这道题属于岛屿题目的低配版
* 这题类似于 200. 岛屿的数量。差别在于，岛屿的数量要将图中的所有点全部遍历一遍，而本题只需要遍历目标点所在的色块
* 定义 DFS 函数：从一个目标像素开始执行染色, 并会对上下左右四个像素递归地进行染色。
* 结束递归的条件是: 
* ➀ 当前遍历的点超出了边界 
* ➁ 它不是起始点的颜色, 就直接返回。同样的, 对于已经染成新颜色的节点也不会继续递归
? 链接：https://leetcode.cn/problems/flood-fill/solution/bfs-he-dfs-liang-chong-bian-li-fang-shi-by-hyj8/

"""


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        targetColor = image[sr][sc]
        # * 如果新旧颜色相同, 不用处理, 直接返回
        if targetColor == color:
            return image

        def traverse(rowIdx, colIdx):
            # * 判断是否超出边界
            if inArea(rowIdx, colIdx) == False:
                return

            # * 判断这个位置是否已经处理过
            if image[rowIdx][colIdx] != targetColor:
                return

            # * 将颜色替换
            image[rowIdx][colIdx] = color
            # * 深度优先搜索四周的像素点
            traverse(rowIdx + 1, colIdx)
            traverse(rowIdx - 1, colIdx)
            traverse(rowIdx, colIdx + 1)
            traverse(rowIdx, colIdx - 1)

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < len(image) and 0 <= colIdx < len(image[0])

        traverse(sr, sc)
        return image


print(Solution().floodFill(image=[[1, 1, 1], [1, 1, 0],
                                  [1, 0, 1]], sr=1, sc=1, color=2))
