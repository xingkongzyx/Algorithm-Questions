""" 
* 本题是使用哈希法的经典题目, 而0015.三数之和, 0018.四数之和 并不合适使用哈希法, 因为这两道题目使用哈希法在不超时的情况下做到「对结果去重」是很困难的, 很有多细节需要处理。
* 
* 而这道题目是四个独立的数组, 只要找到 "A[i] + B[j] + C[k] + D[l] = 0" 就可以, 不用考虑有重复的四个元素相加等于0的情况
? https://leetcode.cn/problems/4sum-ii/solution/454-si-shu-xiang-jia-iimapzai-ha-xi-fa-zhong-de-2/

* 采用分为两组, HashMap 存一组, 另一组和 HashMap 进行比对。
/ 算法时间复杂度为 O(n^2)。
? 链接: https://leetcode-cn.com/problems/4sum-ii/solution/chao-ji-rong-yi-li-jie-de-fang-fa-si-shu-xiang-jia/

"""


class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        record = {}

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum = nums1[i] + nums2[j]
                record[sum] = record.get(sum, 0) + 1

        res = 0
        for m in range(len(nums3)):
            for n in range(len(nums4)):
                sum = nums3[m] + nums4[n]
                target = 0 - sum
                if target in record:
                    res += record[target]

        return res
