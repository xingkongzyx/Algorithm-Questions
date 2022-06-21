//* 相对于动态规划：122.买卖股票的最佳时机II 本题只需要在计算卖出操作的时候减去手续费就可以了，代码几乎是一样的。
/* 
/ dp[i][0] 表示第i天持有股票状态所获得的最大利润。 dp[i][1] 表示第i天不持有股票状态所得最大利润
/ 与122的区别就在于第i天不持有股票即dp[i][1]的情况，它可以由两个状态推出来 
/   1. 第i-1天就不持有股票，那么就保持现状，所得利润就是昨天不持有股票的所得利润 即：dp[i - 1][1]
/   2. 第i天卖出股票，所得利润就是按照今天股票价格卖出后所得现金，
    > 注意这里需要有手续费了即：dp[i - 1][0] + prices[i] - fee
*/
var maxProfit = function (prices, fee) {
    let dp = new Array(prices.length).fill([0, 0]);
    dp[0][0] = -prices[0];
    dp[0][1] = 0;

    for (let i = 1; i < prices.length; i++) {
        dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] - prices[i]);
        dp[i][1] = Math.max(
            dp[i - 1][1],
            dp[i - 1][0] + prices[i] - fee
        );
    }

    return dp[prices.length - 1][1];
};
