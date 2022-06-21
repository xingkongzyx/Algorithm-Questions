//? leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/best-time-to-buy-and-sell-stock-ii-zhuan-hua-fa-ji/
/* 
* 关键是想到最终利润是可以分解的，即使是连续上涨交易日，以 [1,2,3,4] 为例，这 4 天的股价依次上升，得到的最大利润是：
* res =  prices[3] - prices[0]
*     =  (prices[3]-prices[2]) + (prices[2]-prices[1]) + (prices[1]-prices[0])
* 等价于每天都买卖
* 算法流程：遍历整个股票交易日价格列表 price，策略是所有上涨交易日都买卖（赚到所有利润），所有下降交易日都不买卖（永不亏钱）。
! 通过遍历prices, 只要知道今天的价格比昨天升了，我们就假设我们昨天买了股票，然后今天卖出。如果今天比昨天降了，则不买卖。如果遇到连续几天的股价都在上升，我们也拆解为每天买入/卖出
> 局部最优：收集每天的正利润，全局最优：求得最大利润。
*/
https: var maxProfit = function (prices) {
    let result = 0;
    for (let i = 1; i < prices.length; i++) {
        let profit = prices[i] - prices[i - 1];
        if (profit > 0) result += profit;
    }

    return result;
};
