/// 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 个台阶，2 个台阶，3 个台阶，.......，直到 m 个台阶。问有多少种不同的方法可以爬到楼顶呢？

/*
 * 1. 确定dp数组以及下标的含义
 *   dp[i] 表示爬到第i阶台阶一共有 dp[i]种方法
 * 2. 确定递推公式
 *   dp[i] = dp[i] + dp[i - 1] + dp[i - 2] + ... dp[i - m]; m <= i
 * 3. dp数组如何初始化
 *   dp[0] = 1
 * 4. 确定遍历顺序
 *   排列问题，外层循环为到达的位置，内层循环为从0到m的步数
 */
var climbStairs = function (n) {
    let maxDistancePerStep = 2;
    let dp = new Array(n + 1).fill(0);
    dp[0] = 1;

    for (let position = 1; position <= n; position++) {
        for (let step = 1; step <= maxDistancePerStep; step++) {
            if (step <= position) dp[position] += dp[position - step];
        }
    }

    return dp[n];
};

console.log(climbStairs(5));
