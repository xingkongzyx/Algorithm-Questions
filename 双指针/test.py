class Solution:
    def threeSumClosest(self, nums, target):

        nums.sort()
        rSum = 0
        minDiff = float('inf')
        for i in range(len(nums) - 1):
            firstNum = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currentSum = firstNum + nums[left] + nums[right]
                currentDiff = abs(currentSum - target)
                if currentDiff < minDiff:
                    minDiff = currentDiff
                    rSum = currentSum
                if currentSum == target:
                    return currentSum
                elif currentSum < target:
                    left += 1
                else:
                    right -= 1
        return rSum
print(Solution().threeSumClosest(nums = [0,0,0], target = 1))
