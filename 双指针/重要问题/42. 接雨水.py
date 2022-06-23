""" 
* 双指针法比较好的讲解:
? https://leetcode.cn/problems/trapping-rain-water/solution/shuang-zhi-zhen-by-lafiteee-aay8/
? https://leetcode.cn/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode/327718
* 这里得出结论: 对于左指针 left, 它右侧的真实的最大值 >= rightMax, 对于右指针 right, 它左侧的真实的最大值 >= leftMax.
"""
class Solution(object):
    def trap(self, height):
        totalWater = 0
        left = 1
        right = len(height) - 2
        leftMax = height[0]
        rightMax = height[-1]
        while left <= right:
            if leftMax < rightMax:
                #* 对于左指针 left, 它「右侧的真实的最大值」 >= rightMax, 而对于一个位置来说影响它接水的应该是『左右两侧最大值中的较小值』, 对于左指针所在位置来说, 如果确定它「左侧真实的最大值 leftMax」小于「右侧不确定的最大值 rightMax」, 「右侧真实的最大值」又是大于等于 「右侧不确定的最大值 rightMax」, 所以对于这个位置来说它的接水量一定是 leftMax - height[left]
                currentHeight = height[left]
                if currentHeight < leftMax:
                    totalWater += leftMax - currentHeight
                
                leftMax = max(leftMax, height[left])
                left += 1
            else:
                #* 对于右指针 right, 它「左侧的真实的最大值」 >= leftMax, 而对于一个位置来说影响它接水的应该是『左右两侧最大值中的较小值』, 对于右指针所在位置来说, 如果确定它「右侧真实的最大值 rightMax」小于「左侧不确定的最大值 leftMax」, 「左侧真实的最大值」又是大于等于「左侧不确定的最大值 leftMax」, 所以对于这个位置来说它的接水量一定是 rightMax - height[right]
                currentHeight = height[right]
                if currentHeight < rightMax:
                    totalWater += rightMax - currentHeight
                rightMax = max(rightMax, height[right])
                right -= 1
        return totalWater
    
print(Solution().trap(height = [4,2,0,3,2,5]))
