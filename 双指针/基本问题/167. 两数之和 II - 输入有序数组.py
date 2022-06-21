
#? O(n) 的双指针解法的本质原理 https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/solution/yi-zhang-tu-gao-su-ni-on-de-shuang-zhi-zhen-jie-fa/ 
class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]

res = Solution().twoSum(numbers = [-1,0], target = -1)
print(res)
