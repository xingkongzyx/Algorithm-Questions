/* 
状态0: 买入股票状态，可能是今天买入，也可能是以前就持有了股票
状态1：不持有股票状态，并且两天前就卖出了股票，度过了冷冻期，并且一直没有新的操作，处于不持有股票状态。要达到这个状态，要不前一天是冷冻期 dp[i-1][3]; 要不前一天就是度过了冷冻期的不持有状态 dp[i-1][1]
状态2：不持有股票状态，并且是今天卖出的股票. 只可能是从昨天持有股票状态转移而来 dp[i-1][0]. 而不能从昨天不持有股票状态(昨天卖出) dp[i-1][2] 的状态转移，因为这之间需要冷冻期
状态3：冷冻期，只能持续一天. 只能从昨天卖出股票状态转移 dp[i-1][2]

*/
var maxProfit = function (prices) {
    if (prices.length < 1) {
        return 0;
    }
    let numOfDays = prices.length;
    let dp = new Array(numOfDays);
    for (let i = 0; i < numOfDays; i++) {
        dp[i] = new Array(4).fill(0);
    }
    dp[0][0] = -prices[0];
    for (let i = 1; i < numOfDays; i++) {
        dp[i][0] = Math.max(
            dp[i - 1][0],
            dp[i - 1][1] - prices[i],
            dp[i - 1][3] - prices[i]
        );
        dp[i][1] = Math.max(dp[i - 1][3], dp[i - 1][1]);
        dp[i][2] = dp[i - 1][0] + prices[i];
        dp[i][3] = dp[i - 1][2];
    }
    // console.log(dp);
    return Math.max(
        dp[numOfDays - 1][1],
        dp[numOfDays - 1][2],
        dp[numOfDays - 1][3]
    );
};
const prices = [1, 2, 3, 0, 2];
maxProfit(prices);
