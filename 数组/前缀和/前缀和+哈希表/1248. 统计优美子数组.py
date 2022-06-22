
""" 
? https://leetcode.cn/problems/count-number-of-nice-subarrays/solution/tong-ji-you-mei-zi-shu-zu-by-leetcode-solution/
# lc 560 是求『和为 K 的子数组』, 这个题目是让我们求『恰好有 k 个奇数数字的连续子数组』, 这两个题几乎是一样的, 上个题中我们将前缀区间的和保存到哈希表中, 这个题目我们只需将前缀区间的奇数个数保存到区间内即可。

* 先求取 nums 中奇数个数的前缀和 preSum, 即 preSum[i] 表示nums数组中前 i 个数有多少个奇数。注意前 0 个数代表 nums[0], 这里假设前缀和数组与 nums 的索引完全对应. 则对于每一个子数组 nums[j...i], 区间中的奇数个数可以采用 「preSum[i] - preSum[j-1]」 求得。
* 则问题转换成 560 的解法, 其中 preSum[i] - preSum[j - 1] = k, 虑以 i 结尾的「优美子数组」个数时只要统计有多少个奇数个数为 preSum[i] - k 的 preSum[j] 即可

/ 时间复杂度：O(n)，其中 nn 为数组的大小。我们只需要遍历一遍数组即可求得答案。

/ 空间复杂度：O(n)，其中 nn 为数组的大小。频次hashmap 记录的最大值不会超过 n ，因此只需要额外的 O(n) 的空间。


"""
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        from collections import defaultdict

        #* 这里的前缀和统计的是到 nums[i] 为止(包括这个元素)总共拥有的 "奇数" 元素的个数之和
        preSum = 0
        
        map = defaultdict(int)
        
        map[0] = 1
        count = 0
        for i in range(len(nums)):
            currentNum = nums[i]
            if currentNum % 2 == 1:
                #* 如果当前元素是奇数, 更新preSum
                preSum += 1
            
            if preSum - k in map:
                count += map[preSum - k]
                
            map[preSum] += 1
        
        return count
