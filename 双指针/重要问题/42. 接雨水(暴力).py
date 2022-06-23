
# ? https://leetcode.cn/problems/trapping-rain-water/solution/bao-li-jie-fa-yi-kong-jian-huan-shi-jian-zhi-zhen-/
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        totalWater = 0
        
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            currentHeight = height[i]
            # 找寻左测最高的
            leftIdx = i - 1
            leftMaxHeight = height[leftIdx]
            while leftIdx >= 0:
                currentLeftHeight = height[leftIdx]
                if currentLeftHeight > leftMaxHeight:
                    leftMaxHeight = currentLeftHeight
                leftIdx -= 1
                
            # 找寻右侧最高的
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
            # print(f"for idx {i}, totalWater = {totalWater}, currentWater is {currentWater}")
        return totalWater
    
print(Solution().trap(height = [4,2,0,3,2,5]))
