/* 
/ 链接：https://leetcode-cn.com/problems/combination-sum-iv/solution/gong-shui-san-xie-yu-wan-quan-bei-bao-we-x0kn/
/ 与 518. 零钱兑换 II 的区别：https://leetcode-cn.com/problems/coin-change-2/solution/dong-tai-gui-hua-wan-quan-bei-bao-wen-ti-by-liweiw/

* 本题与「完全背包求方案数」问题的差别在于：选择方案中的不同的物品顺序代表不同方案。
* 
* 举个 🌰，在「完全背包」问题中，凑成总价值为 6 的方案 [1,2,3] 算是 1 种方案，但在本题算是 3 * 2 * 1 = 6 种方案（[1,2,3],[2,1,3],[3,1,2] ... ）。
* 
* 因此我们不能直接代入「完全背包」的思路（状态定义）来求解。
! 而在零钱兑换问题中 dp[i][j] 为考虑前 i 件物品，凑成总和为 j 的方案数量。
! 对于第 i 个硬币我们有两种决策方案：
! 1. 不使用该硬币：
!     dp[i - 1][j]
! 2. 使用该硬币：由于每个硬币可以被选择多次（容量允许的情况下），因此方案数量应当是选择「任意个」该硬币的方案总和：
!  dp[i−1][j−1∗nums[i]] + dp[i−1][j−2∗nums[i]] + dp[i−1][j−3∗nums[i]] +...+ dp[i−1][j−(j/nums[i])∗nums[i]] 

* 定义 dp[i][j] 为从nums[0:i]中任意选择元素，凑成总和为 j 的方案数是多少。
* 
> 在这道题中，对任意的 dp[当前组合长度][target] 而言，组合中的最后一个数字可以选择 nums[0:i] 之间的任意数值，因此 dp[当前组合长度][target] 应该为以下所有方案总和：
* 
* 最后一个数选择 nums[0]，方案数为 dp[len][target - nums[0]]
* 最后一个数选择 nums[1]，方案数为 dp[len][target - nums[1]]
* 最后一个数选择 nums[2]，方案数为 dp[len][target - nums[2]]

# 注意: 要在本层的基础上进行加法操作，如果本层没有任何满足的元素，则直接用上层的值dp[len-1][target]。用本层元素加的原因是本层才会考虑新的元素 nums[i], 在nums[i] 出现的基础上j也会有新的排序数
*/
var combinationSum4 = function (nums, target) {
    let dp = new Array(nums.length);

    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(target + 1).fill(0);
    }

    for (let i = nums[0]; i <= target; i += nums[0]) {
        dp[0][i] = 1;
    }

    dp[0][0] = 1;
    console.log(dp);
    for (let i = 1; i < nums.length; i++) {
        for (let j = 0; j <= target; j++) {
            // 有的数它属于nums[0,i]之间任何元素都无法对其产生新的组合，所以直接使用上一行的值
            let currentPosHasChanged = false;
            for (let idx = 0; idx <= i; idx++) {
                if (j >= nums[idx]) {
                    dp[i][j] += dp[i][j - nums[idx]];
                    currentPosHasChanged = true;
                }
            }
            if (currentPosHasChanged === false)
                dp[i][j] = dp[i - 1][j];
        }
    }
    // console.log(dp);
    return dp[nums.length - 1][target];
};
console.log(combinationSum4([1, 2, 3], 4));
