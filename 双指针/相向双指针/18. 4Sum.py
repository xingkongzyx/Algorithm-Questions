"""  
* 为了避免枚举到重复四元组，则需要保证每一重循环枚举到的元素不小于其上一重循环枚举到的元素，且在同一重循环中不能多次枚举到相同的元素。
* 为了实现上述要求，可以对数组进行排序，并且在循环过程中遵循以下两点：
# 每一种循环枚举到的下标必须大于上一重循环枚举到的下标； 
# 同一重循环中，如果当前元素与上一个元素相同，则跳过当前元素(注释中的两次去重操作)。
? https://leetcode.cn/problems/4sum/solution/si-shu-zhi-he-by-leetcode-solution/
"""


class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            # ! 去重操作 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                # ! 去重操作 2
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
                        result.append(
                            [firstNum, secondNum, thirdNum, fourthNum])

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


print(Solution().fourSum(nums=[2, 2, 2, 2, 2], target=8))
