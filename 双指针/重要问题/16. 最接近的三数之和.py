class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        minDiff = float('inf')
        closedSum = 0
        for i in range(0, len(nums) - 2):
            currentNum = nums[i]
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                numSum = currentNum + nums[left] + nums[right]
                diff = abs(numSum - target)
                
                if diff < minDiff:
                    closedSum = numSum
                    minDiff = diff
                
                if numSum > target:
                    right -= 1
                elif numSum < target:
                    left += 1
                else:
                    return closedSum
        return closedSum    
# -4 -1 1 2
res = Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1)
print(res)
