""" 
* 不确定缺失具体情况的nums内部部分用二分；超过的部分是可以直接计算的
? 必看: https://leetcode.cn/problems/missing-element-in-sorted-array/solution/you-xu-shu-zu-zhong-de-que-shi-yuan-su-by-leetcode/
? 代码借鉴: https://leetcode.cn/problems/missing-element-in-sorted-array/solution/1060-you-xu-shu-zu-zhong-de-que-shi-yuan-su-by-klb/
? https://leetcode.cn/problems/missing-element-in-sorted-array/solution/python3-jian-zhi-er-fen-fa-by-accsrd-ssij/
"""

class Solution(object):
    def missingElement(self, nums, k):
        def countMissNum(idx):
            # * 计算到 nums[idx] 为止总共缺失的数字个数
            correctNum = nums[idx] - nums[0] + 1
            actualNum = idx - 0 + 1
            missNum = correctNum - actualNum
            return missNum
        
        
        # * 如果 k 比缺口大，则直接返回结果，时间复杂度O(1)
        if (k > countMissNum(len(nums) - 1)):
            return nums[-1] + k - countMissNum(len(nums) - 1)

        # * 
        left = 0
        right = len(nums) - 1
        # * 难处理的是nums中间缺失的部分，因为不知道缺失的具体分布，所以用二分搜索找到第一个到当前位置的缺口元素的数量大于等于 k 的元素下标
        while left < right:
            mid = left + ((right - left) >> 1)
            curMisNum = countMissNum(mid)
            if curMisNum < k:
                left = mid + 1
            else:
                right = mid
        # * 最后从 nums[left] 的上一个元素 nums[left - 1] 计算: 还需要往前走几步能够满足missing number 的数量恰好等于 k. 需要获得 idx= left - 1 时的缺口数量, 然后计算 k 比其大多少, 大的数字就是需要从 nums[left - 1] 起步要在增加的大小
        return nums[left - 1] + k - countMissNum(left - 1)
