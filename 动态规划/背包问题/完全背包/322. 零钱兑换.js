/*
 * 1. 确定dp数组以及下标的含义
 *   dp[i] 表示对于此时的金额 i 最少的硬币个数
 * 2. 确定递推公式
 *   dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1)
 * 3. dp数组如何初始化
 *   dp[0] = 0 剩下的初始化为 infinity
 * 4. 确定遍历顺序
 * 本题求钱币最小个数，那么钱币有顺序和没有顺序都可以，都不影响钱币的最小个数。
 * 所以本题并不强调集合是组合还是排列。
 ! 如果求组合数就是外层for循环遍历物品，内层for遍历背包。 如果求排列数就是外层for遍历背包，内层for循环遍历物品。
 > 所以本题的两个for循环的关系是：外层for循环遍历物品，内层for遍历背包或者外层for遍历背包，内层for循环遍历物品都是可以的！
 *   我采用外层循环coins array，内层循环为从1到amount
 */

var coinChange = function (coins, amount) {
    let dp = new Array(amount + 1).fill(Infinity);
    dp[0] = 0;

    for (
        let currentAmount = 1;
        currentAmount <= amount;
        currentAmount++
    ) {
        for (let j = 0; j < coins.length; j++) {
            if (coins[j] <= currentAmount) {
                dp[currentAmount] = Math.min(
                    dp[currentAmount],
                    dp[currentAmount - coins[j]] + 1
                );
            }
        }
    }

    return dp[amount] === Infinity ? -1 : dp[amount];
};
