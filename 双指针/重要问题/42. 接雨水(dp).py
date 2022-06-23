
# ? https://leetcode.cn/problems/trapping-rain-water/solution/bao-li-jie-fa-yi-kong-jian-huan-shi-jian-zhi-zhen-/
""" 
/ 时间复杂度: O(n)。
/ 空间复杂度: O(n)，用来保存每一列左边最高的墙和右边最高的墙。
! 暴力解法中, 对于每一列, 我们求它左边最高的墙和右边最高的墙, 都是重新遍历一遍所有高度, 这里我们可以优化一下。
* 通过一次遍历，把已经扫过的柱形高度的最大值记录下来，具体如下: 
* 从左向右: 记录当前遍历位置左侧（不包括当前位置的）最高高度；
* 从右向左: 记录当前遍历位置右侧（不包括当前位置的）的最高高度。

* leftHighest[i]: 数组 height 在区间 [0, i - 1] 中的最大值；
* rightHighest[i]: 数组 height 在区间 [i + 1, len - 1] 中的最大值。

* 递推公式: 
* leftHighest[i] = max(leftHighest[i-1], height[i-1])
* rightHighest[i] = max(leftHighest[i+1], height[i+1])
"""
class Solution(object):
    def trap(self, height):
        leftHighest = [0 for _ in height]
        rightHighest = [0 for _ in height]
        
        for i in range(1, len(height) - 1):
            leftHighest[i] = max(leftHighest[i-1], height[i-1])

        for i in range(len(height) - 2, 0, -1):
            rightHighest[i] = max(height[i+1], rightHighest[i+1])

        totalWater = 0
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            currentHeight = height[i]
            leftMaxHeight = leftHighest[i]
            rightMaxHeight = rightHighest[i]
            minHeight = min(leftMaxHeight, rightMaxHeight)
            if currentHeight < minHeight:
                totalWater += (minHeight - currentHeight)
        return totalWater

print(Solution().trap(height = [4,2,0,3,2,5]))
