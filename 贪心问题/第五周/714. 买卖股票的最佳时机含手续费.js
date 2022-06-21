//* 使用贪心策略，就是最低值买，最高值（如果算上手续费还盈利）就卖。
/*
? 说一下自己对这道题以及122题区别的理解： 为什么122题不需要找最低点和最高点呢？因为122没有手续费！换句话说，每个点都是最低点，但凡下一天价格比它高，那我们就卖！这样最低点又更新为了下一个，在一个连续获利区间内最低点就是在不断更迭，以至于对外我们不需要关心最低点，只需要关心任意两天的利润是否为正！ 本题有手续费了，将会导致即便下一天价格比今天高，但不一定能卖出去！所以我今天这个最低价格要保持住这个状态直到后面的某一个天的售价可以吞下我的价格+手续费了，也就是有利润了，才要更新！而且注意122题的分解根据公式： （ABC连续三天上涨的情况下）A天买入，C天卖出，利润等于C-A-Fee；根据122题的分解公式，我们可以得到这个利润等同于 C-B+B-A-Fee，也就是当连续获利时，手续费只算在某一次交易中即可。 所以当 某一天可以获利（prices[i]-purchasePrice-fee>0）时，purchasePrice要更新为“今天的价格-fee”，这样下一轮如果继续获利，将不会多余的减去fee这个费用！！！如果不继续获利，purchasePrice也要进行变换了，对结果毫无影响

 * 所以我们在做收获利润操作的时候其实有三种情况：
 * 情况一：收获利润的这一天并不是收获利润区间里的最后一天（不是真正的卖出，相当于持有股票），所以后面要继续收获利润。
 * 情况二：前一天是收获利润区间里的最后一天（相当于真正的卖出了），今天要重新记录最小价格了。
 * 情况三：不作操作，保持原有状态（买入，卖出，不买不卖）
 *
 */

var maxProfit = function (prices, fee) {
    let profit = 0;
    let purchasePrice = prices[0];

    for (let i = 1; i < prices.length; i++) {
        let currentPrice = prices[i];
        // 一种是初始情况，发现第二天的价格比第初始化的价格还低，则更新最低价格。或者已经过了股票上升趋势，卖出股票并更新买入价格
        if (currentPrice < purchasePrice) {
            purchasePrice = currentPrice;
        }
        // 此时卖出去连交易费都无法回本，所以不进行任何操作
        if (currentPrice - purchasePrice <= fee) {
            continue;
        }

        // 此时卖出去能够回本，所以卖出股票，
        // 但可能目前仍处于上升区间，我们还需要更新 purchasePrice. 至于 purchasePrice = currentPrice - fee; "-fee"的原因是在同一个上升趋势中 例如 [10,16,19,25] 在计算 16-19, 19-25 的利润时我们不会再减去手续费，只有在第一次 10-16 区间我们才减去了手续费
        // 或者说减去手续费是因为在 prices(k+1) < prices(k+2)-fee < prices(k+3)-fee 的情况下只交一次手续费
        if (currentPrice - purchasePrice > fee) {
            profit += currentPrice - purchasePrice - fee;
            purchasePrice = currentPrice - fee;
        }
    }

    return profit;
};

const prices = [1, 3, 2, 8, 4, 9],
    fee = 2;
console.log(maxProfit(prices, fee));
