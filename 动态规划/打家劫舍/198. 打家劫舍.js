//! 比【代码随想录还详细】https://leetcode-cn.com/problems/house-robber/solution/da-jia-jie-she-dong-tai-gui-hua-jie-fa-b-m3kl/
/*
 * 1. 确定dp数组（dp table）以及下标的含义
 * dp[i]表示偷窃包含下标i的房屋所能偷到的最大金额是dp[i]
 * 2. 确定递推公式
 * 决定dp[i]的因素就是第i房间偷还是不偷。
 * 如果偷第i间房屋   ----> dp[i] = dp[i-2] + nums[i]
 * 如果不偷第i间房屋 ----> dp[i] = dp[i-1]
 * 两者取最大值 max(dp[i-2] + nums[i], dp[i-1])
 *
 * 3. dp数组如何初始化
 * 对于第0间房子，所能偷窃的最大值就是偷它，所以dp[0]就是nums[0]
 * 对于第1间房子，可以不偷它而偷第0间，或者偷他而不偷第0间
 * dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
 *
 * 如果 i = 0 则只有一间房屋，则偷窃该房屋，可以偷窃到最高总金额即，dp[i] = nums[0];
 * 如果 i = 1 则只有两间房屋，则由于两间房屋相邻，不能同时偷窃，只能偷窃其中的一间房屋，因此选择其中金额较高的房屋进行偷窃，可以偷窃到最高总金额即，dp[1] = max(nums[0], nums[1]);
 *
 * 4. 确定遍历顺序
 * 从左到右
 */
var rob = function (nums) {
    if (nums.length == 0) return 0;
    if (nums.length == 1) return nums[0];
    
    let dp = new Array(nums.length);
    dp[0] = nums[0];
    dp[1] = Math.max(nums[0], nums[1]);

    for (let i = 2; i < dp.length; i++) {
        dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
    }

    return dp[nums.length - 1];
};
