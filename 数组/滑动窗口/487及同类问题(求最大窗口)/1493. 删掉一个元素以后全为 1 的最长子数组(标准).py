
#* 使用滑动窗口的原因: 如果找到了一个长度为 L 且删除 1 个字符以后不能保证当前数组范围内全部都是 1 的子数组，那么左边界相同、长度更长的子数组一定不符合要求。符合滑动窗口性质：向右边扩散得到和越来越大，向左边界扩散得到和越来越小。

#> 求最大窗口，所以在窗口非法时「收缩窗口」(也就是移动左指针)，并且在「收缩窗口」的判断句外面记录最大窗口。这道题「窗口非法」就是指窗口内「0 元素的数量」大于1的时候。

#! 这种解法与 487 1004 思路一致，但是中间有无用的缩小滑动窗口的行为. 既然只对最长有效的子数组感兴趣，所以我们的滑动窗口不需要收缩，即使窗口可能覆盖无效的子数组。
class Solution(object):
    def longestSubarray(self, nums):
        ## Step 1
        ## 定义需要维护的变量
        ## 因为是求最大长度, 所以有 maxLen, 又同时涉及计数 (需要从中删掉一个元素 翻译就是 满足条件的子数组中 0 的个数不能超过 1 个), 因为是二进制数组, 不需要哈希表, 只需要记录 0 的个数就可以
        zeroCount = 0
        maxLen = 0
        
        ## Step 2: 定义窗口的首尾端 (left, right), 然后滑动窗口
        ## 每次循环结束后, 窗口 [left, right) 左闭右开区间存储的是只包含最多一个 0 的子数组
        left = 0
        right = 0
        
        ## Step 3: 更新需要维护的变量 (record, maxLen). 
        #! 只要 zeroCount 中记录的 0 的个数「小于等于 1 个」, 说明就可以删除这个 0 得到全是 1  的子数组; 或者如果子数组目前全是 1 (zeroCount 是 0) 也符号要求
        while right < len(nums):
            rightNum = nums[right]
            if rightNum == 0:
                zeroCount += 1
                
            if zeroCount <= 1:
                maxLen = max(maxLen, right - left + 1)

            ## Step 4
            ## 根据题意, 题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            ## 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            ## 当 zeroCount 大于 1 的时候，窗口不合法
            ## 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (zeroCount)
            while zeroCount > 1:
                # print("move left")
                leftNum = nums[left]
                if leftNum == 0:
                    zeroCount -= 1
                left += 1
            right += 1   
        return maxLen - 1
print(Solution().longestSubarray(nums = [1,1,1]))
