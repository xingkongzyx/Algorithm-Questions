""" 
! 完全平方数就是物品(可以无限件使用), 要凑成的正整数n就是背包容量, 问凑满这个背包最少有多少物品？

 * 1. 确定dp数组以及下标的含义
 *   dp[j] 表示凑成和为 n 的完全平方数的最少数量是 dp[j]
 * 2. 确定递推公式
 *   dp[j] = Math.min(dp[j], dp[j - nums[i]] + 1)
 * 3. dp数组如何初始化
 *   dp[0] = 0 剩下的数初始化为 infinity
 * 4. 确定遍历顺序
 *   所以本题并不强调集合是组合还是排列。所以本题的两个for循环的关系是: "外层for循环遍历物品, 内层for遍历背包" 或者 "外层for遍历背包, 内层for循环遍历物品"都是可以的!
 *   我采取 外层for循环遍历完全平方数, 内层for遍历 target
"""


class Solution:
    def numSquares(self, n):

        # 预处理出 <=sqrt(n) 的完全平方数
        nums = []
        i = 1
        while i*i <= n:
            nums.append(i*i)
            i += 1

        # 转化为完全背包问题【套用「322. 零钱兑换」】
        target = n
        dp = [target] * (target+1)    # 初始化为一个较大的值, 如 +inf 或 n
        dp[0] = 0    # 合法的初始化；其他 dp[j]均不合法

        # 完全背包: 优化后的状态转移
        for num in nums:                        # 第一层循环: 遍历nums
            for j in range(num, target+1):      # 第二层循环: 遍历背包【正序】
                dp[j] = min(dp[j], dp[j-num] + 1)

        return dp[target]
