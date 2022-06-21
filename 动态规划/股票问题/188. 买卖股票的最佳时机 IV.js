var maxProfit = function (k, prices) {
    let numOfDays = prices.length;
    if (numOfDays === 0) return 0;
    let dp = new Array(numOfDays);
    for (let i = 0; i < numOfDays; i++) {
        dp[i] = new Array(2 * k + 1).fill(0);
    }

    for (let i = 1; i < dp[0].length; i++) {
        if (i % 2 === 1) {
            dp[0][i] = -prices[0];
        } else {
            dp[0][i] = 0;
        }
    }
    // console.log(dp);
    for (let i = 1; i < numOfDays; i++) {
        for (let j = 1; j < dp[i].length; j++) {
            // 在第i天属于持有状态，要么是前一天就是持有态，要么是在第i天购买的股票
            if (j % 2 === 1)
                dp[i][j] = Math.max(
                    dp[i - 1][j],
                    dp[i - 1][j - 1] - prices[i]
                );
            else
                dp[i][j] = Math.max(
                    dp[i - 1][j],
                    dp[i - 1][j - 1] + prices[i]
                );
        }
    }
    // console.log(dp);
    return dp[numOfDays - 1][2 * k];
};
const k = 3,
    prices = [2, 6, 8, 7, 8, 7, 9, 4, 1, 2, 4, 5, 8];
maxProfit(k, prices);
