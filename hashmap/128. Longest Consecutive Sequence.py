""" 
? 必看: https://leetcode.cn/problems/longest-consecutive-sequence/solution/jian-ming-yi-dong-de-javajie-da-by-lan-s-pf26/

# 不能「排序」再使用滑动窗口的原因在于题目中 nums = [0,1,1,2] 时，应该返回中间隔着一个 1 的 [0,1,2], 而不是 [1,2]

* 最直观的做法是考虑枚举数组中的每个数 x, 考虑以其为起点, 不断尝试匹配 x+1, x+2, ⋯ 是否存在, 假设最长匹配到了 x+y, 那么以 x 为起点的最长连续序列即为 x, x+1, x+2, ..., x+y, 其长度为 y+1, 我们不断枚举并更新答案即可。
* 但仔细分析这个过程, 我们会发现其中执行了很多不必要的枚举, 如果已知有一个 x, x+1, x+2, ⋯, x+y 的连续序列, 而我们却重新从 x+1, x+2 或者是 x+y 处重新开始尝试匹配, 那么得到的结果肯定不会优于枚举 x 为起点的答案, 因此我们在外层循环的时候碰到这种情况跳过即可。

# 但都有哪些数可以成为连续序列的左边界呢？
* 设想, 如果 num 为一个左边界, 那么 num - 1 就不应该存在于数组中(因为如果num - 1存在于数组中, num - 1又与num连续, 所以num不可能是连续序列的左边界)。
* 因此如果一个数字 num 满足: num-1不存在于数组中。这个数字num就可以成为连续序列的左边界。


/ 外层循环需要 O(n) 的时间复杂度, 只有当一个数是连续序列的第一个数的情况下才会进入内层循环, 然后在内层循环中匹配连续序列中的数, 因此数组中的每个数只会进入内层循环一次。根据上述分析可知, 总时间复杂度为 O(n), 符合题目要求。
? 官解的讲解也非常好: https://leetcode.cn/problems/longest-consecutive-sequence/solution/zui-chang-lian-xu-xu-lie-by-leetcode-solution/

"""


class Solution(object):
    def longestConsecutive(self, nums):
        record = set()
        for num in nums:
            record.add(num)

        maxLen = 0
        for num in record:
            # * 如果 num - 1 存在于set中, 那么 num 不可能是左边界, 直接跳过
            if (num - 1) in record:
                continue
            # * 此时, num 会是一个左边界, 我们再不断地查找 num+1, num+2, ... 是否存在于set中, 来看以num为左边界的连续序列能有多长
            curLen = 0
            while num in record:
                num += 1
                curLen += 1
            # * 在上述遍历中, 我们知道了对于每一个可能的左边界, 能扩出的最长连续序列的长度, 再在这些长度中取最大即为结果。
            maxLen = max(curLen, maxLen)

        return maxLen
