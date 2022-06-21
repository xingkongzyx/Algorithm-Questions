/* 
dp[i][j] = x 表示，戳破气球 i 和气球 j 之间（开区间，不包括 i 和 j）的所有气球，可以获得的最高分数为 x。

那么根据这个定义，题目要求的结果就是 dp[0][n+1] 的值

链接：https://leetcode.cn/problems/burst-balloons/solution/dong-tai-gui-hua-tao-lu-jie-jue-chuo-qi-qiu-wen-ti/


*/
var maxCoins = function (nums) {
    /// 两端加入两个虚拟气球, 现在可以戳破的气球的索引变成了从 1 到 nums.length
    let newNumsArr = new Array(nums.length + 2);
    newNumsArr[0] = 1;
    newNumsArr[nums.length + 1] = 1;

    for (let i = 1; i <= nums.length; i++) {
        newNumsArr[i] = nums[i - 1];
    }
    let arrLen = newNumsArr.length;
    let dp = new Array(arrLen);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(arrLen).fill(0);
    }
    for (let i = arrLen - 1; i >= 0; i--) {
        /// j 应该从左往右
        for (let j = i + 1; j < arrLen; j++) {
            /// k为 i 和气球 j 之间的所有气球都中可能最后被戳破的那一个
            for (let k = i + 1; k < j; k++) {
                /// 对于一组给定的 i 和 j，我们只要穷举 i < k < j 的所有气球 k，选择得分最高的作为 dp[i][j] 的值即可
                dp[i][j] = Math.max(
                    dp[i][j],
                    dp[i][k] +
                        dp[k][j] +
                        newNumsArr[i] * newNumsArr[j] * newNumsArr[k]
                );
            }
        }
    }
    return dp[0][arrLen - 1];
};

nums = [3, 1, 5, 8];
maxCoins(nums);
