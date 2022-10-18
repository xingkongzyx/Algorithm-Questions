""" 
* 由于湍流子数组是输入数组「连续」的子区间，「连续」很重要。并且：
* 在左边界固定的前提下，如果长度为 L 的连续子区间，不构成湍流子数组，那么，左边界相同，且长度更长的子数组一定不是湍流子数组；
? https://leetcode.cn/problems/longest-turbulent-subarray/solution/zui-chang-tuan-liu-zi-shu-zu-by-leetcode-zqoq/
"""


class Solution(object):
    def maxTurbulenceSize(self, arr):
        if len(arr) < 2:
            return 1
        maxLen = 0

        left = 0
        # * 因为要向前看一个位置, 所以从 1 开始
        right = 1
        # * 表示在 「right」与「right - 1」这个比较的前一个比较的结果(也就是「right - 1」与「right - 2」对应元素的比较结果)，只有两个比较的结果是不同的并且 nums[right] != nums[right-1] 才能构成湍流子数组
        preCheck = False

        while right < len(arr):
            currentCheck = arr[right] < arr[right - 1]
            if currentCheck == preCheck:
                left = right - 1

            #! 特殊情况, 如果两个元素相等是可能有 preCheck != curCheck 的情况的，如果没有下面的判断，我们计算最长湍流子数组时将出现bug.
            #! 因为湍流子数组不可能包含两个相同的数，所以湍流子数组只能再次从 right 位置开始重新计算。
            if arr[right] == arr[right - 1]:
                left = right
            # > 这时候滑动窗口内包含合法的湍流子数组了
            maxLen = max(maxLen, right - left + 1)
            preCheck = currentCheck
            right += 1

        return maxLen


print(Solution().maxTurbulenceSize(arr=[9, 4, 2, 10, 7, 8, 8, 1, 9]))
