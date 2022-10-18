""" 
* 假设目前数组总和为 sum, 我们需要的移动次数为 m, 那么整体数组总和将会增加 m*(n-1), n 是数组的长度, 因为每轮有 n-1 个元素被加 1, 一共有 m 轮, 总和增加的结果是上面的公式。
* 又因为最后数组所有元素都相等, 假设值为 target, 于是有: 
* ➀ n * target = m * (n - 1) + sum(nums). 右侧的值为通过移动增加的值加上原来的数组的和
* 再设原数组中最小的元素为 min_val, 则得到了:
* ➁ target = m + min_val 

! 为什么呢, 因为对于最小值, 你每次的递加都必须对原列表的最小值加一, 每次操作中必须覆盖最小值, m 次操作后, 最小值就变为了 min(nums) + m, 该值就是最后的相同值
# 为什么每次 +1 操作都必须覆盖 min_val; 可以这样理解: 
# 若某次操作漏掉了 min_val, 而对其他数全部 +1, 那么最小值与其他数之间的差距会变得更大, 那么此次操作可以说是无效的；

* 最后将 ➁ 代入公式 ➀, 得到最后的公式: 
* m = sum - min_val * n

? https://leetcode.cn/problems/minimum-moves-to-equal-array-elements/solution/python3-yi-xing-dai-ma-ji-bai-99-diao-ch-25ar/
? https://leetcode.cn/problems/minimum-moves-to-equal-array-elements/solution/shu-xue-ti-by-powcai-2/

"""


class Solution:
    def minMoves(self, nums) -> int:
        minVal = min(nums)
        sumVal = sum(nums)
        return sumVal - minVal * len(nums)
