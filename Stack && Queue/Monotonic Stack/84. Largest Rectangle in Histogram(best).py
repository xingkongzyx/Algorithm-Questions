""" 
? 为什么头尾加两个0: https://leetcode.cn/problems/largest-rectangle-in-histogram/solution/wo-yong-qiao-miao-de-bi-yu-jiang-dan-diao-zhan-jie/ 
* 原数组首部加入一个0: 解决弹出栈顶元素以后, 栈空了, 无法找到它的左边界(新的栈顶索引),从而无法计算以弹出的栈顶元素为高的长方形面积； 原数组尾部加入一个0: 解决栈内元素递增, 且数组已经遍历到尾部, 此时没有机会计算以栈内元素为高的长方形面积
? 为什么使用单调栈: https://leetcode.cn/problems/largest-rectangle-in-histogram/solution/dong-hua-yan-shi-dan-diao-zhan-84zhu-zhu-03w3/

? 必看讲解: https://leetcode.cn/problems/largest-rectangle-in-histogram/solution/bao-li-jie-fa-zhan-by-liweiwei1419/
#* 从左到右遍历柱子, 对于每一个柱子, 我们想找到第一个高度小于它的柱子, 那么我们就可以使用一个「单调递增栈」来实现。如果「当前遍历到的柱子的高度」大于栈顶元素代表的柱子的高度」, 那么说明不是我们要找的柱子, 我们把它塞进去继续遍历。如果「当前遍历到的柱子的高度」小于「栈顶元素代表的柱子的高度」, 那么我们就找到了第一个小于的柱子。对于「栈顶元素代表的柱子的高度」, 其「右边第一个」小于它的就是当前遍历到的柱子, 左边第一个小于它的就是栈中下一个要被弹出的元素, 因此以「栈顶元素代表的柱子的高度」为最矮柱子所能延伸的最大矩形面积为『栈顶元素代表的柱子的高度 * (当前遍历到的柱子索引 - 栈中下一个要被弹出的元素索引 - 1)』
/ 时间复杂度: O(n), 因为对于每个柱子只会经历入栈出栈, 所以最多 2n 次。
/ 空间复杂度: O(n), 栈的大小。
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        heights = [0] + heights + [0]
        maxArea = 0
        stack = []

        for i in range(len(heights)):
            # 如果栈不为空且当前考察的元素值小于栈顶元素值, 则表示以栈顶元素值为高的矩形面积可以确定
            while len(stack) and heights[i] < heights[stack[-1]]:
                topIdxInStack = stack.pop()
                # 获取栈顶元素对应的高
                curHeightOfTopIdx = heights[topIdxInStack]
                # 栈顶元素弹出后, 新的栈顶元素就是其左侧边界
                leftIdx = stack[-1]
                # 右侧边界是当前正在遍历的索引
                rightIdx = i
                # 计算以「curHeightOfTopIdx」为高的矩形面积, 并与已经记录的最大值进行比较
                curArea = (rightIdx - leftIdx - 1) * curHeightOfTopIdx
                maxArea = max(curArea, maxArea)
            stack.append(i)
        return maxArea
# Solution().largestRectangleArea([1,2,3])
