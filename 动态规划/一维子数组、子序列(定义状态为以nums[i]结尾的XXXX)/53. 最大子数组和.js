/* 
* dp[i] 以 nums[i] 结尾的连续子数组的最大和是dp[i] 
> dp数组的含义都与 674, 300 是非常相似的
! 这里状态的定义不是题目中的问题的定义，不能直接将最后一个状态返回回去；这个问题的输出是把所有的 dp[0]、dp[1]、……、dp[n - 1] 都看一遍，取最大值。 同样的情况也适用于「力扣」第 300 题，第 674 题

* 状态转移方程（描述子问题之间的联系）
* 根据状态的定义，由于 nums[i] 一定会被选取，并且以 nums[i] 结尾的连续子数组与以 nums[i - 1] 结尾的连续子数组只相差一个元素 nums[i] 。

* 假设数组 nums 的值全都严格大于 0，那么一定有 dp[i] = dp[i - 1] + nums[i]。可是 dp[i - 1] 有可能是负数，于是分类讨论：
*   1. 如果 dp[i - 1] > 0，那么可以把 nums[i] 直接接在 dp[i - 1] 表示的那个数组的后面，得到和更大的连续子数组；因为加上一个大于0的数永远会使得最后的结果更大
*   2. 如果 dp[i - 1] <= 0，那么 nums[i] 加上前面的数 dp[i - 1] 以后值不会变大。于是 dp[i] 「另起炉灶」，此时单独的一个 nums[i] 的值，就是 dp[i]。 因为加上小于0的数会使得最后的结果更小

? 非常经典的讲解，一定要看 https://leetcode.cn/problems/maximum-subarray/solution/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai/

*/

var maxSubArray = function (nums) {
    let dp = new Array(nums.length);

    dp[0] = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (dp[i - 1] <= 0) dp[i] = nums[i];
        else if (dp[i - 1] > 0) dp[i] = nums[i] + dp[i - 1];
    }
    let res = Math.max(...dp);
    return res;
};
