
# 
#* 时间复杂度： O(n²)。数组中的每个元素都需要向左向右扫描。
#* 空间复杂度 O(1) 的额外空间

""" 
? 暴力解法的示例图总结的非常好: https://leetcode.cn/problems/trapping-rain-water/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-8/
* 按列求每一列能装的水. 求每一列的水, 只需要关注当前列, 以及左边最高的墙, 右边最高的墙就够了。装水的多少, 根据木桶效应, 只需要看左边最高的墙和右边最高的墙中较矮的一个就够了。但如果〖较矮的墙的高度小于等于当前列的墙的高度〗, 正在求的列不会有水


"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        totalWater = 0
        #* 最两端的列不用考虑，因为一定不会有水。
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            currentHeight = height[i]
            #* 找寻左测最高的墙
            leftIdx = i - 1
            leftMaxHeight = height[leftIdx]
            while leftIdx >= 0:
                currentLeftHeight = height[leftIdx]
                if currentLeftHeight > leftMaxHeight:
                    leftMaxHeight = currentLeftHeight
                leftIdx -= 1
                
            #* 找寻右侧最高的墙
            rightIdx = i + 1
            rightMaxHeight = height[rightIdx]
            while rightIdx < len(height):
                currentRightHeight = height[rightIdx]
                if currentRightHeight > rightMaxHeight:
                    rightMaxHeight = currentRightHeight
    
                rightIdx += 1    

            minHeight = min(leftMaxHeight, rightMaxHeight)
            currentWater = (minHeight - currentHeight) * 1
            if currentHeight < minHeight:
                totalWater += currentWater

        return totalWater
    
print(Solution().trap(height = [4,2,0,3,2,5]))
