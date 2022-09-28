""" 
* 要想使得操作次数最小, 我们应当「尽可能减少 nums 1 中元素的值, 同时尽可能增加 nums 2 ​中元素的值」
* 重点: 题主把下降的值用 num-1 也变成上升了, 比如相差是8, 用两个5超过了, 返回2次。因为用5可以超过或相等, 那么5可以只升3, 一定可以得到答案。
* freq[i] 代表的是最多能增加/减少i, 比如我最后 i = 4 把 diff = 2 变成了 -2 由于是最多调整4, 那么这次我可以调整 2 让diff变成 0, 对最后次数不产生影响。

* 增大nums1的一个数, 就等于减小nums2中的一个数。
* 在有多个数可以选择的情况下, 增大时应该优先增大较小的数（上升空间大）; 同理, 减小时应当优先减小较大的数（下降空间大）。



? https://leetcode.cn/problems/equal-sum-arrays-with-minimum-number-of-operations/solution/tong-guo-zui-shao-cao-zuo-ci-shu-shi-shu-o8no/
"""


class Solution:
    def minOperations(self, nums1, nums2) -> int:
        # * 获取两个数组的和
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        if sum1 == sum2:
            return 0

        # * 调整顺序, 使得 num1 的和永远是大于 num2 的
        if sum1 < sum2:
            sum2, sum1 = sum1, sum2
            nums2, nums1 = nums1, nums2

        freq = [0] * 6

        # # 因为 nums2 的和是小于 nums1 的和的, 所以对于 nums1 来说, 要使得它的和与 nums2 的和相同, 最少操作次数的方法就是减少值。因为 The values in the arrays are between 1 and 6, inclusive. 所以每个元素可以减少的最大的值是 nums1[i] - 1
        for i in range(len(nums1)):
            num1Decrease = nums1[i] - 1

            freq[num1Decrease] += 1

        # # 因为 nums2 的和是小于 nums1 的和的, 所以对于 nums2 来说, 要使得它的和与 nums1 的和相同, 最少操作次数的方法就是增加值。因为 The values in the arrays are between 1 and 6, inclusive. 所以每个元素可以增加的最大的值是 6 - nums2[j]
        for j in range(len(nums2)):
            num2Increase = 6 - nums2[j]
            freq[num2Increase] += 1

        diff = sum1 - sum2
        res = 0
        for i in range(5, 0, -1):
            while freq[i] > 0 and diff > 0:
                diff -= i
                freq[i] -= 1
                res += 1

        return res if diff <= 0 else -1
