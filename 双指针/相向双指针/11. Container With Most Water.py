""" 
? 暴力解法: https://leetcode.cn/problems/container-with-most-water/solution/yuan-lai-hui-luo-ji-qing-xi-jian-dan-yi-hbxc2/

# ? 双指针法的正确性 https://leetcode.cn/problems/container-with-most-water/solution/on-shuang-zhi-zhen-jie-fa-li-jie-zheng-que-xing-tu/
# 先确定最大的宽度，然后记录当前的面积，此时如果左边的柱子短些，那么就可以抛弃了，因为左边的这根柱子跟其他右边的柱子一定不会再有更大的面积了；所以我们替换掉短板去寻找可能存在的更大的面积。
"""


class Solution(object):
    def maxArea(self, height):
        maxArea = 0

        left = 0
        right = len(height) - 1

        while left < right:
            leftHeight = height[left]
            rightHeight = height[right]
            minHeight = min(leftHeight, rightHeight)
            # * 水的宽度是两根柱子之间的距离，水的高度是两根柱子较短的那一根的高度
            # * 如果固定「短」的柱子，移动「长」的柱子，那么水的高度一定不会增加，且宽度一定减少，所以水的面积一定减少。这个时候，「短」的柱子和任意一个其他柱子的组合，其实都可以排除了。也就是我们可以排除掉「短」的柱子了。
            #! 这个排除掉「短」柱子的操作，就是双指针代码里的〚left += 1 or right -= 1〛。left 和 right 两个指针中间的区域都是还未排除掉的区域。随着不断的排除，left 和 right 都会往中间移动。当 left 和 right 相遇，算法就结束了。

            currentArea = minHeight * (right - left)
            maxArea = max(maxArea, currentArea)

            if minHeight == leftHeight:
                left += 1
            else:
                right -= 1

        return maxArea


print(Solution().maxArea(height=[1, 1]))
