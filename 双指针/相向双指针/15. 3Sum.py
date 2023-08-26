
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
            # * 如果最小的数大于0则不可能三个数的和为0, 直接退出
            if currentNum > 0:
                return result
            
            # * 当 i > 0且 "nums[i] == nums[i - 1]" 时即跳过此元素 nums[i]：因为已经将 nums[i - 1] 的所有组合加入到结果中，本次双指针搜索只会得到重复组合。例如当 a === d 时，a + b + c = d + b + c = 0, 寻找下一个不同的数
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
                    #! 我觉得最重要的一点 如果不加 left < right 这个判断条件, 遇到 [0, 0, 0, 0] 的情况 会一直执行 left += 1 到达数组最后一个位置, 在加上判断后的更新指针操作, 最终导致索引溢出的情况发生
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # * 上面进行检查更新后，此时左右指针的位置在左右最后一个相同的数上，需要再前进/后退一步，到达第一个不同的位置
                    left += 1
                    right -= 1
                elif leftNum + rightNum > target:
                    right -= 1
                else:
                    left += 1
                    
            
        return result
    
print(Solution().threeSum(nums = [0,0,0]))  
