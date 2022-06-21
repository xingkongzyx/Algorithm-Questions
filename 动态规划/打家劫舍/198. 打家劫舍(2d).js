/* 
* 某一间房子 i 存在两种状态
*  ✧ 抢劫了
*  ✧ 未抢劫
* 所以我们定义二维数组 dp[i][0] 表示第 i 间房子没抢劫，dp[i][1] 表示第 i 间房子抢劫了

* 如果第 i 间房子抢劫了，那么前一间房子必然未抢劫，所以第 i 间房子抢劫了的收益为
* dp[i][1] = dp[i-1][0] + nums[i]

* 如果第 i 间房子没抢劫，不知道i-1是否能偷，偷也不违背相邻原则，所以就会有个择优。第 i 间房子没抢，则可以第 i-1 间房子也没有抢，也可以是 i-1 间房子抢了，所以 dp[i][0] = max(dp[i-1][0], dp[i-1][1])
? 二维讲解: https://leetcode.cn/problems/house-robber/solution/198-da-jia-jie-she-by-alexer-660/
*/
var rob = function (nums) {
    // dp[i][0]: 不偷取index 为 i 的房子能够偷的的最高金额 dp[i][0] = max(dp[i-1][0], dp[i-1][1])
    // dp[i][1]: 偷取index 为 i 的房子能够偷的的最高金额 dp[i][0] = nums[i] + dp[i-1][0]

    const dp = new Array(nums.length);

    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(2).fill(0);
    }

    dp[0][0] = 0;
    dp[0][1] = nums[0];

    for (let i = 1; i < dp.length; i++) {
        dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]);
        dp[i][1] = nums[i] + dp[i - 1][0];
    }
    let lastIdx = nums.length - 1;
    return Math.max(dp[lastIdx][0], dp[lastIdx][1]);
};

console.log(rob([2, 7, 9, 3, 1]));
