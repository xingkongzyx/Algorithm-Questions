var change = function (amount, coins) {
    let dp = new Array(amount + 1).fill(0);
    dp[0] = 1;
    // # 为什么两层循环的顺序不能颠倒? 简单来说, 先枚举金额, 代表对于金额来说每次硬币循环都是可以的, "1+2" 和 "2+1" 代表了两种方案, 是排列数. 但是先枚举硬币, 那么只是对相应的金额进行方案添加, 之前的硬币使用后不能再次使用. 也就是说 "1+2" 可行, 但是 "2+1" 就不会再出现, 得到的结果是组合数, 也就是零钱兑换的方案
    for (let i = 0; i < coins.length; i++) {
        for (let j = coins[i]; j <= amount; j++) {
            dp[j] += dp[j - coins[i]];
        }
    }

    return dp[amount];
};
const amount = 5;
const coins = [1, 2, 5];
change(amount, coins);
