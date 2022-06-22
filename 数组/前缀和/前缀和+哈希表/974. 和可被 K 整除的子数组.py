""" 
? 比较好的汇总: https://leetcode.cn/problems/subarray-sums-divisible-by-k/solution/shu-zu-zheng-chu-wen-ti-hui-zong-qian-zh-5ocu/

* 元素和能被 K 整除的子数组数目 翻译就是:
* 『有几种i、j组合, 使得 nums[i] 到 nums[j] 之和 mod K == 0』
* ↓ ↓ ↓ 转化为 ↓ ↓ ↓
* 有几种 i、j 组合, 满足 (preSum[j] - preSum[i-1]) mod K== 0。
* 有几种 i、j 组合, 满足 preSum[j] mod K == preSum[i-1] mod K。
* 前提: preSum[j] 、preSum[i-1] 为正整数。负数的情况要处理。
? https://leetcode.cn/problems/subarray-sums-divisible-by-k/solution/you-jian-qian-zhui-he-na-jiu-zai-ci-dai-ni-da-tong/


* 上面提到的关键的性质: 对于两个数 a 和 b, 如果有 (a - b) % k == 0, 那么 a % k == b % k。

# 对原数组进行遍历, 逐个计算到达每个元素位置时的前缀和以及『该前缀和对 k 的余数』 modRes, 并将 modRes 及其 它的出现频次 记录在哈希表中。如果存在两个前缀和对 k 的 mod 相等, 也就是 "当相同的模值出现第二次时", 表示第一次出现位置之后到第二次出现位置的子数组的和能被 K 整除。
? https://leetcode.cn/problems/subarray-sums-divisible-by-k/solution/974-qian-zhui-he-he-ke-bei-k-zheng-chu-d-5ozp/

"""
class Solution(object):
    def subarraysDivByK(self, nums, k):
        from collections import defaultdict

        #* 这里的前缀和储存的是到nums[i]为止(包括这个元素)的前缀和
        preSum = 0
        
        map = defaultdict(int)
        #* 如果 preSum[i] = k，则 preSum[i] % k == 0，说明以 nums[i] 为尾的前面的所有元素构成的子数组的和 能够被 k 整除。这个场景也要计算，所以，需要将hash表的边界条件设置为 map[0] = 1。
        map[0] = 1
        
        count = 0
        for i in range(len(nums)):
            preSum += nums[i]
            modRes = preSum % k
            #* 因为这道题求的是被 k 整除的子数组, map 中存储的是「preSum % k」的结果而不是像 560 那样存储的是子数组和
            if modRes in map:
                count += map[modRes]

            map[modRes] += 1
        return count

Solution().subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5)

