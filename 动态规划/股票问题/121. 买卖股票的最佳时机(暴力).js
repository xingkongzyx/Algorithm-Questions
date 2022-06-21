var maxProfit = function (prices) {
    let result = 0;
    // 外层遍历买入的日期，内层遍历卖出的日期
    for (let i = 0; i < prices.length - 1; i++) {
        for (let j = i + 1; j < prices.length; j++) {
            let boughtPrice = prices[i];
            let soldPrice = prices[j];
            result = Math.max(result, soldPrice - boughtPrice);
        }
    }

    return result;
};
