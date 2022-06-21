/* 
? 卡尔的拓展讲解https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-iii-by-6472/ 

* 要求最多买卖两次，那么每天都会有五种状态：不买、买一次、卖一次、买两次、卖两次。
* 而这五种状态赚的钱的转换规律为：
* 
* 总不买 = 0；
* 买一次 = 买过一次，这次不卖 *或者* 没买过，　这次买。
* 卖一次 = 卖过一次，这次不买 *或者* 买过一次，这次卖。
* 买两次 = 买过两次，这次不卖 *或者* 卖过一次，这次买。
* 卖两次 = 卖过两次，没机会了 *或者* 买过两次，这次卖。

链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/solution/wei-liao-xie-chu-hao-kan-you-ji-yi-li-ji-cn38/


*/
var maxProfit = function (prices) {
    let dp = new Array(prices.length).fill([0, 0, 0, 0, 0]);
    dp[0][0] = 0;
    //# 第一次买入
    dp[0][1] = -prices[0];
    //# 第一次卖出
    dp[0][2] = 0;
    //# 第二次买入 关于为什么第二次买入初始化为-prices[0]，因为题目规定最多交易2次不代表一定只能交易2次，也有可能只交易一次。 因此此时就从第二次买入的状态开始动态规划，之后就不会交易了即只交易了一次。 那么既然是从第二次买入的状态开始，那他初始值也必须是在第一天买下股票
    dp[0][3] = -prices[0];
    //# 第二次卖出
    dp[0][4] = 0;

    for (let i = 1; i < prices.length; i++) {
        //# 0状态表示  “从未持有”，故第i天仍是从未持有状态意味着i-1天也从未持有
        dp[i][0] = dp[i - 1][0];
        //# 1状态表示第一次持有，但状态转移可以有两种：1.继承前一天的持有，当天不动作，因而仍是第一次持有状态；2.前一天从未持有，但当天买入
        dp[i][1] = Math.max(dp[i - 1][1], dp[i - 1][0] - prices[i]);
        //# 2状态表示第一次清仓，状态转移可以有两种：1.前一天已经清仓了，但当天不动作，因而仍然第一次清仓状态；2.前一天第一次持有，但当天卖出
        dp[i][2] = Math.max(dp[i - 1][2], dp[i - 1][1] + prices[i]);
        dp[i][3] = Math.max(dp[i - 1][3], dp[i - 1][2] - prices[i]);
        dp[i][4] = Math.max(dp[i - 1][4], dp[i - 1][3] + prices[i]);
    }
    //# 这是最后的得失，如果买了两次，一定处于二次卖出状态，如果没买满两次，二次卖出状态和一次的状态也是相同的
    return dp[prices.length - 1][4];
};
