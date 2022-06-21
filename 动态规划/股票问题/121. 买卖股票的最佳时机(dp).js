/* 
* 1. 确定dp数组（dp table）以及下标的含义
* dp[i][0] 表示第i天持有股票所得最大的利润
* dp[i][1] 表示第i天不持有股票所得最大的利润

* 2. 确定递推公式
* 第i天持有股票 有可能是之前就持有了 ==> dp[i][0] = dp[i-1][0]
* 第i天持有股票 也有可能是当天买入的 ==> dp[i][0] = -prices[i]

* 第i天不持有股票 有可能是之前就不持有股票 ==> dp[i][1] = dp[i-1][1]
* 第i天不持有股票 有可能是当天卖出了       ==> dp[i][1] = prices[i] + dp[i-1][0]
* "prices[i] + dp[i-1][0]" 使用加号的原因是当我们在持有的操作时dp[i-1][0] = -prices[i] 此时它是负数，我们要算利润，就直接用当天的价格加上这个负数实际上就相当于减的操作

* 3. dp数组如何初始化
* dp[0][0] = -prices[0]
* dp[0][1] = 0

* 4. 确定遍历顺序
* 从前向后
*/
var maxProfit = function (prices) {
    let dp = new Array(prices.length);
    for (let i = 0; i < prices.length; i++) {
        dp[i] = new Array(2).fill(0);
    }
    dp[0][0] = -prices[0];
    dp[0][1] = 0;

    for (let i = 1; i < dp.length; i++) {
        dp[i][0] = Math.max(dp[i - 1][0], -prices[i]);
        dp[i][1] = Math.max(dp[i - 1][1], prices[i] + dp[i - 1][0]);
    }

    return Math.max(
        dp[prices.length - 1][0],
        dp[prices.length - 1][1]
    );
};
