# https://leetcode.cn/problems/3sum/solution/3sumpai-xu-shuang-zhi-zhen-yi-dong-by-jyd/
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
