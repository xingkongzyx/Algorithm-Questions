
# * 枚举以每个柱形的高度为当前矩形的高度的最大矩形的面积。我们可以使用一重循环枚举某一根柱子，将其固定为矩形的高度 h。随后我们从这跟柱子开始向两侧延伸，直到遇到高度小于 h 的柱子，就确定了矩形的左右边界。如果左右边界之间的宽度为 w，那么对应的面积为 w×h。

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        for i in range(len(heights)):
            # * 固定高度，向两边扩散
            curHeight = heights[i]

            # * 左边看一下，看最多能向左延伸多长，找到「大于等于」当前柱形高度的「最左边元素」的下标;
            leftCount = 0
            leftIdx = i - 1
            while leftIdx >= 0 and heights[leftIdx] >= curHeight:
                leftCount += 1
                leftIdx -= 1

            # * 右边看一下，看最多能向右延伸多长; 找到「大于等于」当前柱形高度的「最右边元素」的下标。
            rightCount = 0
            rightIdx = i + 1
            while rightIdx < len(heights) and heights[rightIdx] >= curHeight:
                rightCount += 1
                rightIdx += 1

            curArea = (leftCount + rightCount + 1) * curHeight
            maxArea = max(curArea, maxArea)

        return maxArea
