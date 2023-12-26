/* 
* 题目中的可 + 或 - 组合数字具有一定迷惑性，可以转化为数组中有哪些数字要在前面放 + 来解题，剩下部分自然是前面放 - 。
* 
* 设 + 部分数组和为：x， - 部分数字和为：y，可以推出 x + y = target(因为y是前面放-的数字的总和,本身就是负数,所以 x-y=target; 后面的 x - y = sum)，x - y = sum（nums），合并可得：x = (target + sum（nums）) // 2。
* 
* 这样就把复杂的可 + 可 - 问题转为只需计算 + 部分的问题，故把x作为新的target，
* 题目其实就变成是：我们需要从数组中找出和为 x 有几种组合方式（这样的话就把什么负数的给去掉了，不然搞得很麻烦一样）
! 也就是从 nums 中选择数字，使得这些数字和为x, 求的就是这样的选择有几种
* 

/ 使用二维数组的理解: https://leetcode-cn.com/problems/target-sum/solution/mu-biao-he-by-nehzil-x5am/

*/

var findTargetSumWays = function (nums, target) {
    let sum = 0;
    for (let num of nums) sum += num;
    //# 如果 abs(target) 大于sum，不可能实现，返回0
    if (Math.abs(target) > sum) return 0;
    //# 如果x不是整数，也就是 target + sum不是偶数，不可能实现，返回0
    if ((sum + target) % 2 === 1) return 0;

    let bagWeight = (sum + target) / 2;
    //# dp[j] 表示：填满 j（包括j）这么大容积的包，有dp[j]种方法
    let dp = new Array(bagWeight + 1).fill(0);
    dp[0] = 1;

    //! 当前填满容量为j的包的方法数 = 之前填满容量为j的包的方法数 + 之前填满容量为j - num的包的方法数. 也就是当前数num的加入，可以把之前和为j - num的方法数加入进来。
    // dp[capacity] += dp[capacity - nums[i]]：
    // 1、如果不选第i个数（nums[i]）的话，则方法数为dp[capacity]；
    // 2、如果选第i个数（nums[i]）的话，则方法数为dp[capacity - nums[i]]；
    //  所以方法总数为：dp[capacity] = dp[capacity] + dp[capacity - nums[i]]；
    for (let i = 0; i < nums.length; i++) {
        for (
            let capacity = bagWeight;
            capacity >= nums[i];
            capacity--
        ) {
            dp[capacity] += dp[capacity - nums[i]];
        }
    }

    return dp[bagWeight];
};
