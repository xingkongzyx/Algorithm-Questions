//! 必看讲解: https://leetcode.cn/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/

/* 
* 基于「动态规划」的状态设计需要满足「无后效性」的设计思想，可以将状态定义为「以 nums[i] 结尾 的「上升子序列」的长度」。
* 
* 「无后效性」的设计思想：让不确定的因素确定下来，以保证求解的过程形成一个逻辑上的有向无环图。这题不确定的因素是某个元素是否被选中，而我们设计状态的时候，让 nums[i] 必需被选中，这一点是「让不确定的因素确定下来」，也是我们这样设计状态的原因。

/ dp[i] 表示：以 nums[i] 结尾 的「上升子序列」的长度。注意：这个定义中 nums[i] 必须被选取，且必须是这个子序列的最后一个元素；

# 不能返回最后一个状态值，最后一个状态值只表示以 nums[len - 1] 结尾的「上升子序列」的长度，状态数组 dp 的最大值才是题目要求的结果。
*/

var lengthOfLIS = function (nums) {
    let result = 1;
    let dp = new Array(nums.length).fill(1);
    for (let i = 1; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] > nums[j]) dp[i] = Math.max(dp[j] + 1, dp[i]);
        }
        result = Math.max(result, dp[i]);
    }
    // console.log(dp);
    return result;
};
nums = [1, 3, 6, 7, 9, 4, 10, 5, 6];
lengthOfLIS(nums);
