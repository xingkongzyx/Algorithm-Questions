""" 
* 数组实际上可以分为三段, 有序+无序+有序, 且两段有序肯定有前面一段都小于后面一段的, 只需要确定「无序的边界」就可以。维护一个 maxVal 一个 minVal 来帮助确定边界。maxVal 和 minVal  并非数组中的最大值最小值, 而是我们路途中遇到的最大值最小值
* ➀ 从左往右走, 如果是「有序」的, maxVal 值一定会连续增加; 若不增加, 说明这一段无序。maxVal 初始值为 nums[0], 因为我们是从左往右走
* ➁ 从右往左走, 如果是「有序」的, minVal 值一定会连续降低; 若不降低, 说明这一段无序。minVal  初始值为 nums[len-1], 因为我们是从右往左走
* 因此, 我们可以「两次」遍历, 从而找出「无序」的左右边界
* ❶ 第一次: 正序遍历, 找到最后一个值小于我们连续更新的 maxVal 值的位置
* ❷ 第二次: 逆序遍历, 找到最后一个值大于我们连续更新的 minVal 值的位置 
? https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/solution/581-zui-duan-wu-xu-lian-xu-zi-shu-zu-si-8rivt/
? https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/solution/si-lu-qing-xi-ming-liao-kan-bu-dong-bu-cun-zai-de-/1194164
? https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/solution/java-shuang-zhi-zhen-shuang-xiang-bian-l-etqf/
/ 时间复杂度: O(n), 其中 n 是给定数组的长度, 我们仅需要遍历该数组两次。
/ 时间复杂度: O(1)。我们只需要常数的空间保存若干变量
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        maxVal = nums[0]
        minVal = nums[length - 1]
        #* 双指针: 用于确认「无序」的左右边界 
        startIdx = 0
        endIdx = 0

        for i in range(1, length):
            if nums[i] >= maxVal:
                maxVal = nums[i]
            else:
                endIdx = i

        
        for i in range(length - 2, -1, -1):
            if nums[i] <= minVal:
                minVal = nums[i]
            else:
                startIdx = i

        #* 如果最后左右指针所在位置相等, 说明原数组就是有序的, 返回 0 即可。
        if startIdx == endIdx:
            return 0
        else:
            return endIdx - startIdx + 1
