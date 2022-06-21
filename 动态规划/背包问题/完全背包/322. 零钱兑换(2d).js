/* 
! 必看文章: https://leetcode.cn/problems/coin-change/solution/by-flix-su7s/ 
/ dp[i][j] 指从 coins[0-i]中选择硬币(每个硬币可以选择多个)，能够凑成金额j的最少硬币个数是 dp[i][j]

/ dp[i][j] = (dp[i-1][j], dp[i-1][j-m*coin[i]] + m) 加上m是因为我们用m枚 nums[i] 硬币替换掉一定数量的 nums[i-1] 的硬币

/ 因为我们需要的是最小值，所以所有的数值最开始都初始化为 Infinity， 
/ 然后对于第一行进行初始化， dp[0][0] = 0 代表想要凑成 amount = 0, 我们不需要硬币，也就是0枚
/ 剩下的第一行的其他位置与 coins[0] 进行比较得到需要用coins[i] 凑成它的数量

/ 遍历: 左到右，上到下
*/
var coinChange = function (coins, amount) {
    let dp = new Array(coins.length);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(amount + 1).fill(Infinity);
    }

    for (let i = coins[0]; i <= amount; i += coins[0]) {
        neededCoins = i / coins[0];
        dp[0][i] = neededCoins;
    }
    dp[0][0] = 0;

    for (let i = 1; i < dp.length; i++) {
        for (let j = 0; j <= amount; j++) {
            //* 无论 j 是否大于 nums[i], j都应该先复制上一行的值
            dp[i][j] = dp[i - 1][j];
            if (j >= coins[i]) {
                //* 计算出目前的j最多能由几枚价值为 coins[i] 的硬币组成，然后对每种由不同数量 coins[i] 硬币组成j的方法进行对比，取最小值
                maxCoins = Math.floor(j / coins[i]);
                while (maxCoins > 0) {
                    dp[i][j] = Math.min(
                        dp[i][j],
                        dp[i - 1][j - maxCoins * coins[i]] + maxCoins
                    );
                    maxCoins -= 1;
                }
            }
        }
    }

    //* 如果的cell的值还是infinity，说明无法使用提供的硬币凑成amount，返回-1
    if (dp[coins.length - 1][amount] === Infinity) return -1;
    else return dp[coins.length - 1][amount];
};
//# 为什么不像使用一维数组解决问题时，运用公式 dp[j] = Math.min(dp[j], dp[j-coins[i]] + 1)呢？在二维数组这相当于 Math.min(dp[i-1][j], dp[i-1][j-coins[i]] + 1), 为什么递推公式不是它呢? 因为在用一维数组时，我们每次使用 j-coins[i] 能够得到的是本次使用 coins[i] 的结果，而在二维数组中，我们使用的是dp[i-1]。这个时候我们得到的是上次使用 coins[i-1] 的结果。而在本次使用 coins[i] 更新 dp[i][j前面的index] 的结果时, dp[i][j] 用的依然是 dp[i-1][*] 的结果，而不能基于使用新的 cOins[i] 的结果进行更新，所以必须计算 coins[i] 的个数，然后在 dp[i-1] 中 看 dp[i-1][j-m*coins[i]] + m 的最小值
