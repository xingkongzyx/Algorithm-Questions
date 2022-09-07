/*
 * dp[i][0]表示，到当前位置，以「降序」结尾的「摆动数组」的最长子序列的长度
 * dp[i][1]表示，到当前位置，以「升序」结尾的「摆动数组」的最长子序列的长度
 ? https://leetcode.cn/problems/wiggle-subsequence/solution/dong-tai-gui-hua-by-cheungq-6-yhvj/
 */
var wiggleMaxLength = function (nums) {
    let dp = new Array(nums.length);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(2).fill(0);
    }

    dp[0][0] = 1;
    dp[0][1] = 1;

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) {
            // * 如果当前是「升序」的话，则当前位置的「以升序结尾」的最长摆动子序列的长度可以由之前的「降序最长摆动子序列」的长度加1，此时的降序继续继承前一个状态的长度。
            dp[i][1] = dp[i - 1][0] + 1;
            dp[i][0] = dp[i - 1][0];
        } else if (nums[i] < nums[i - 1]) {
            // * 如果当前是「降序」的话，则当前位置的「以降序结尾」的最长摆动子序列的长度可以由之前的「升序最长摆动子序列」的长度加1，此时的升序继续继承前一个状态的长度。
            dp[i][1] = dp[i - 1][1];
            dp[i][0] = dp[i - 1][1] + 1;
        } else {
            dp[i][1] = dp[i - 1][1];
            dp[i][0] = dp[i - 1][0];
        }
    }

    return Math.max(dp[nums.length - 1][0], dp[nums.length - 1][1]);
};
