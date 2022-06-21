/*
 * 1. 每一个位置都有 2 个阶梯，1 个阶梯上一层楼，另 1 个阶梯上两层楼；
 * 2. 上两个阶梯的体力值耗费是一样的，但是在不同位置消耗的体力值是不一样的；
 * 3. 楼层顶部在数组之外。如果数组长度为 len，那么楼顶就在下标为 len 的位置
 */

var minCostClimbingStairs = function (cost) {
    // ! dp[i] 表示到索引为 i 位置再选择向上爬一共需要的体力开销。
    const dp = new Array(cost.length);
    dp[0] = cost[0];
    dp[1] = cost[1];

    for (let index = 2; index < cost.length; index++) {
        dp[index] =
            Math.min(dp[index - 1], dp[index - 2]) + cost[index];
    }
    //# 相当于到达倒数第一节台阶和倒数第二节台阶还想往上爬到顶层，所以把这两个值进行比较，但此时计算到达顶层时不需要再加cost了，因为从这两个台阶再迈一步的花费已经包含在(dp[cost.length - 1], dp[cost.length - 2])中了，只需要比较这两个哪个更小
    return Math.min(dp[cost.length - 1], dp[cost.length - 2]);
};

const costs = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1];
console.log(minCostClimbingStairs(costs));
