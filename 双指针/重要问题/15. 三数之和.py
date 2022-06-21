
#? https://leetcode.cn/problems/3sum/solution/3sumpai-xu-shuang-zhi-zhen-yi-dong-by-jyd/
""" 
* 如果我们对有序数组中〖求两数和为定值〗的算法熟悉的话, 我们会很快找到正确的思路。nums 是一个从小到大有序排列的数组, 找出数组中所有两数之和为定值 target的数对。这本质是一个搜索问题, 因为我们必须遍历数组, 把所有可能情况考虑进去, 当然, 用两个for循环能用 O(n²) 的时间复杂度完成目标, 但是这就没有利用到数组是有序的特点。其实, 我们可以从数组的两端同时进行搜索, 这就是双指针的由来。
"""
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums) - 1):
            currentNum = nums[i]
            
            if currentNum > 0:
                return result
            
            if i > 0 and currentNum == nums[i-1]:
                continue
            
            target = 0 - currentNum
            
            left = i + 1
            right = len(nums) - 1

            while(left < right):
                leftNum = nums[left]
                rightNum = nums[right]
                
                if leftNum + rightNum == target:
                    result.append([currentNum, leftNum, rightNum])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif leftNum + rightNum > target:
                    right -= 1
                else:
                    left += 1
                    
            
        return result
    
print(Solution().threeSum(nums = [0,0,0]))  
