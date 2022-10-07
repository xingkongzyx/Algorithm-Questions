""" 
* 数组的两端nums[-1] = nums[n] = -∞ 都是负无穷, 因此数组无论是『单调递增』还是『单调递减』, 又或者是成『起伏状』, 数组中必定包含一个峰值。如下图所示：

* 因为数组中的峰值不止一个, 我们找到任意一个即可。题目还告诉我们对于所有有效的i都有 nums[i] != nums[i + 1], 即数组中的『任意两个相邻数』都不相等。nums[mid] 与 nums[mid + 1] 之间只存在大于以及小于两种情况, 见下方的链接
? 图解: https://leetcode.cn/problems/find-peak-element/solution/er-fen-cha-zhao-zui-jian-jie-yi-dong-de-cvn1f/

? 题目证明: https://leetcode.cn/problems/find-peak-element/solution/xun-zhao-feng-zhi-shun-xu-er-fen-zhuan-h-cyn9/


* 来自大鹏图解的评论区: 这道题, 最重要的是条件是「两边都是负无穷」, 数组当中可能有很多波峰, 也可能只有一个, 如果尝试画图, 就跟股票信息一样, 没有规律。你这样想, 中点所在地方, 可能是某座山的山峰, 山的下坡处, 山的上坡处, 如果是山峰, 最后会二分终止也会找到, 关键是我们的二分方向, 并不知道山峰在我们左边还是右边, 送你两个字你就明白了, 爬山（没错, 就是带你去爬山）, 如果你往下坡方向走, 也许可能遇到新的山峰, 但是也许是一个一直下降的坡, 最后到边界。但是如果你往上坡方向走, 就算最后一直上的边界, 由于最边界是负无穷, 所以就一定能找到山峰, 总的一句话, 往『递增』的方向上, 二分, 一定能找到, 往「递减」的方向只是可能找到, 也许没有。

"""


class Solution:
    def findPeakElement(self, nums):
        """ 
        * 我们使用二分来做, 每次找出区间的中点mid, 比较 nums[mid] 与 nums[mid + 1] 的大小关系然后不断缩小区间范围, 因为题目中说 nums[i] != nums[i + 1], 所以可以进行有效的判断. 根据排除法, "nums[mid] < nums[mid + 1]" 
        * mid 及其左边一定不存在峰值, 缩小搜索区间为 [mid + 1, right]
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                # * 下一轮搜索区间 [mid + 1, right]
                left = mid + 1
            else:
                # * 下一轮搜索区间 [left, mid]
                right = mid
        return left


Solution().findPeakElement(nums=[1, 2, 3, 1])


""" 
 0 1 2 3 4 5 6
[1,2,1,3,5,6,4]
mid = 3
"""
