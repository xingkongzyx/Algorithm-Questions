""" 
? https://leetcode.cn/problems/maximum-sum-of-two-non-overlapping-subarrays/solutions/1374119/qian-zhui-he-by-a-zhu-8o-9w2a/?orderBy=most_votes
? 注释: https://leetcode.cn/problems/maximum-sum-of-two-non-overlapping-subarrays/solutions/1033156/1031-cchao-100de-qian-zhui-he-jie-fa-by-9omn0/comments/1320100
"""


class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        # firstLen 代表 L 的长度, secondLen 代表 M 的长度
        preSum = [0 for _ in range(len(nums) + 1)]
        n = len(nums)
        for i in range(1, len(preSum)):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        # L在M左侧，枚举M的起始点
        res1 = 0
        temp_L_sum = 0
        for i in range(firstLen, n + 1 - secondLen):
            # 此时 temp_L_sum 的代表的前缀和的范围是 (nums[i-1] + ... + nums[i-firstLen])
            temp_L_sum = max(temp_L_sum, preSum[i] - preSum[i - firstLen])
            # 此时 temp_M_sum 的代表的前缀和的范围是 (nums[i] + nums[i+1] + ... + nums[i+secondLen-1])
            temp_M_sum = preSum[i + secondLen] - preSum[i]
            res1 = max(res1, temp_L_sum + temp_M_sum)

        # M在L左侧，枚举L的起始点
        res2 = 0
        temp_M_sum = 0
        for i in range(secondLen, n + 1 - firstLen):
            # 此时 temp_M_sum 的代表的前缀和的范围是 (nums[i-1] + nums[i-1] + ... + nums[i-secondLen])
            temp_M_sum = max(temp_M_sum, preSum[i] - preSum[i - secondLen])
            # 此时 temp_L_sum 的代表的前缀和的范围是 (nums[i] + ... + nums[i+firstLen-1])
            temp_L_sum = preSum[i + firstLen] - preSum[i]
            res2 = max(res2, temp_L_sum + temp_M_sum)

        res = max(res1, res2)
        return res
