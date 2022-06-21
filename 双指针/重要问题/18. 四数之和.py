class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                firstNum = nums[i]
                secondNum = nums[j]
                
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    thirdNum = nums[left]
                    fourthNum = nums[right]
                    
                    numSum = firstNum + secondNum + thirdNum + fourthNum
                    
                    if numSum == target:
                        result.append([firstNum, secondNum, thirdNum, fourthNum])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                        
                    elif numSum > target:
                        right -= 1
                    elif numSum < target:
                        left += 1
        return result

print(Solution().fourSum(nums = [2,2,2,2,2], target = 8))
