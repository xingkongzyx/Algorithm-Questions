""" 
? https://leetcode.cn/problems/maximal-rectangle/solution/maximal-rectangle-by-ikaruga-idh2/

? 带注释的代码: https://leetcode.cn/problems/maximal-rectangle/solution/js85zui-da-ju-xing-dan-diao-zhan-lian-do-20st/
"""


class Solution:
    def maximalRectangle(self, matrix) -> int:
        heights = [0 for _ in range(len(matrix[0]) + 2)]
        maxArea = 0
        for i in range(len(matrix)):
            # * 遍历每一行时，都计算出以这一行为底的带高度的数组
            for j in range(len(matrix[0])):
                # * 如果当前的值是 1，那么以它为底的矩形的高度就是以上一行的同一列的矩形的高度加 1
                if matrix[i][j] == "1":
                    heights[j + 1] += 1
                elif matrix[i][j] == "0":
                    # * 如果当前的值是 0，那么以它为底的矩形的高度就是 0
                    heights[j + 1] = 0
            # # 使用 84 的方法计算这一行为底的带高度的数组的矩形最大面积
            curArea = self.largestRectangleArea(heights)
            # print(f"curHeight is {heights}, curArea is {curArea}")
            maxArea = max(maxArea, curArea)
        return maxArea

    def largestRectangleArea(self, heights) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            curHeight = heights[i]
            while stack and heights[stack[-1]] > curHeight:
                lastIdx = stack.pop()
                lastHeight = heights[lastIdx]
                curArea = (i - stack[-1] - 1) * lastHeight
                maxArea = max(maxArea, curArea)
            stack.append(i)
        return maxArea


Solution().maximalRectangle([["0", "1"], ["1", "0"]])
