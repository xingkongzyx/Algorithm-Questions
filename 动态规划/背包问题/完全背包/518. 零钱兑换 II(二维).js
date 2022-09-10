// https://leetcode-cn.com/problems/coin-change-2/solution/dong-tai-gui-hua-wan-quan-bei-bao-wen-ti-by-liweiw/
var change = function (amount, coins) {
    //! dp[i][j]表示从区间 [0, i]种硬币中选，且总金额恰好为 j 的所有选法集合的方案数，即为答案。属于组合类动归，可以参考 474. 一和零

    let dp = new Array(coins.length);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(amount + 1).fill(0);
    }

    for (let index = coins[0]; index <= amount; index += coins[0]) {
        dp[0][index] = 1;
    }
    //* 1. dp[0][0] 的值设置为 1，这一点可能比较难理解，但它作为被参考的值，可以使得后续的状态转移方程正确。原因是：当 dp[i - 1][j - k * coins[i]] 的第 2 维 j - k * coins[i] == 0 成立的时候，k 个硬币 coin[i] 恰好成为了一种组合。因此，dp[0][0] = 1 是合理的（代入状态转移方程，值正确）。2. 填写第 1 行（下标为 0 的那一行），也是初始化的时候需要考虑的内容。第 1 行只考虑第 1 枚硬币 coins[0]，能够组合出的容量只有 coins[0] 的整数倍数。

    //* 也可以理解为在背包问题中状态转移过程中我们有两个选择，一个是选择使用coins[0], 一个是不使用coins[0]. 当 j=0 的时候, 不使用coins[0]就符合了条件. 所以 dp[0][0] = 1
    dp[0][0] = 1;

    /*
     * 按照第i种硬币(coins[i])可以选 0个, 1个, 2个, 3个, ..., k个. 划分集合 dp[i][j]。其中 k*coin[i] <= j，也就是说在背包能装下的情况下，枚举第i种硬币可以选择几个。
     *
     * 第i种硬币选 0个，dp[i][j] = dp[i-1][j]
     * 第i种硬币选 1个，dp[i][j] = dp[i-1][j - coins[i]]
     * 第i种硬币选 k个，dp[i][j] = dp[i-1][j - k*coins[i]]
     ! 递推公式： dp[i][j] = dp[i-1][j] + dp[i-1][j-coins[i]] + dp[i-1][j-2*coins[i]] + ... + dp[i-1][j-k*coins[i]] 
     */
    /// 对于遍历到的每一种面值的硬币，逐个考虑添加到 「总金额」 中。由于硬币的个数可以无限选取，因此对于一种新的面值的硬币 coins[i]，依次考虑选取 0 枚、1 枚、2 枚，以此类推，直到选取这种面值的硬币的总金额超过需要的总金额 j 为止。
    for (let i = 1; i < dp.length; i++) {
        for (
            let currentAmount = 0;
            currentAmount <= amount;
            currentAmount++
        ) {
            if (currentAmount >= coins[i]) {
                let counter = Math.floor(currentAmount / coins[i]);
                while (counter > 0) {
                    dp[i][currentAmount] +=
                        dp[i - 1][currentAmount - counter * coins[i]];
                    counter--;
                }
                //* 注意除了使用 coins[i] 的硬币组合数外，我们还需要加上不使用 coins[i] 凑成 currentAmount 时的硬币组合数
                dp[i][currentAmount] += dp[i - 1][currentAmount];
            } else {
                dp[i][currentAmount] = dp[i - 1][currentAmount];
            }
        }
    }
    return dp[coins.length - 1][amount];
};
const amount = 5;
const coins = [1, 2, 5];
change(amount, coins);
