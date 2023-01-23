""" 
* 我们可以分类讨论, 求出按照结束时间排序后的前 i 个工作的最大报酬： 
* ➀ 不选第 i 个工作, 那么最大报酬等于前 i-1 个工作的最大报酬(转换成了一个规模更小的子问题); 
* ➁ 选第 i 个工作, 由于工作时间不能重叠, 设 j 是最大的满足 endTime[j] ≤ startTime[i] 的 j, 那么最大报酬等于前 j 个工作的最大报酬加上 profit[i](同样转换成了一个规模更小的子问题); 
* ➂ 这两种决策取最大值
! 由于按照结束时间排序，前 j 个工作中的任意一个都不会与第 i 个工作的时间重叠。
* 定义 dp [i] 表示按照结束时间排序后的前 i 个工作的最大报酬, dp[i] = max(dp[i-1], dp[j]+profit[i])
? https://leetcode.cn/problems/maximum-profit-in-job-scheduling/solution/dong-tai-gui-hua-er-fen-cha-zhao-you-hua-zkcg/
"""
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append([startTime[i], endTime[i], profit[i]])

        # * 根据工作结束时间进行排序
        jobs.sort(key=lambda x: x[1])

        dp = [0 for _ in range(len(jobs) + 1)]

        # print(jobs)

        for i in range(1, len(dp)):
            # * i 对应的真正的 job index 是 i - 1
            # * 同理，通过 binarySearch 得到的 index 是基于 Job array的，想要让 dp array 进行理解，下标要加 1
            prev_job_ix = self.binarySearchEndTime(
                jobs, i - 1, jobs[i - 1][0]) + 1

            dp[i] = max(dp[i - 1], dp[prev_job_ix] +
                        jobs[i - 1][2])
        # print(dp)
        return dp[-1]

    def binarySearchEndTime(self, start_end_profit_arr, right, targetStartTime):
        # # 寻找小于等于 targetStartTime 的最后一个工作结束时间对应的下标
        # * left 从 -1 开始是因为有可能前面所有的工作都不能满足早于 targetStartTime 之前结束，这时就要返回 -1. 而在调用的时候进行了加 1 操作能使得返回 -1 的时候也能读取 dp[0]
        left = -1
        right = right

        while left < right:
            mid = left + (right - left + 1) // 2
            # 当mid job结束时间大于 targetStartTime 时一定不满足要求，下一轮搜索区间变为 [left, mid - 1]
            if start_end_profit_arr[mid][1] > targetStartTime:
                right = mid - 1
            else:
                # 下一轮搜索区间变为 [mid, right]
                left = mid

        return left


# Solution().jobScheduling(startTime=[1, 2, 3, 3], endTime=[
#     3, 4, 5, 6], profit=[50, 10, 40, 70])
