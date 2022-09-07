/* 
> 局部最优：收集每天的正利润，全局最优：求得最大利润。

* 关键是想到最终利润是可以分解的，即使是连续上涨交易日，以 [1,2,3,4] 为例，这 4 天的股价依次上升，得到的最大利润是：
* res =  prices[3] - prices[0]
*     =  (prices[3]-prices[2]) + (prices[2]-prices[1]) + (prices[1]-prices[0])
* 等价于每天都买卖
* 算法流程：遍历整个股票交易日价格列表 price，策略是所有上涨交易日都买卖（赚到所有利润），所有下降交易日都不买卖（永不亏钱）。
! 该算法仅可以用于计算，但 计算的过程并不是真正交易的过程. 仔细观察上面的式子，按照贪心算法，在下标为 1、2、3 的这三天，我们实际做的操作是买进昨天的，卖出今天的。虽然这种操作题目并不允许，但是它等价于：在下标为 0 的那一天买入，在下标为 3 的那一天卖出。

? https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/solution/tan-xin-suan-fa-by-liweiwei1419-2/
? https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/solution/best-time-to-buy-and-sell-stock-ii-zhuan-hua-fa-ji/
*/
https: var maxProfit = function (prices) {
    let result = 0;
    for (let i = 1; i < prices.length; i++) {
        let profit = prices[i] - prices[i - 1];
        if (profit > 0) result += profit;
    }

    return result;
};
